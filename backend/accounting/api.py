from ninja import Router
from typing import List
from django.shortcuts import get_object_or_404
from django.db import transaction as db_transaction
from ninja.errors import HttpError

from .models import Account, Transaction, JournalEntry
from .schemas import TransactionIn, TransactionOut, AccountSchema

router = Router()


@router.get("/accounts", response=List[AccountSchema])
def list_accounts(request):
    return Account.objects.all()


@router.post("/transactions", response=TransactionOut)
def create_transaction(request, payload: TransactionIn):
    # 1. 驗證借貸平衡
    debit_sum = sum(e.amount for e in payload.entries if e.direction == "DEBIT")
    credit_sum = sum(e.amount for e in payload.entries if e.direction == "CREDIT")

    if debit_sum != credit_sum:
        raise HttpError(400, f"借貸不平衡: 借方 {debit_sum} != 貸方 {credit_sum}")

    # 2. 開啟資料庫交易 (確保主檔和分錄同時成功或失敗)
    with db_transaction.atomic():
        # 建立交易主檔
        tx = Transaction.objects.create(
            date=payload.date, description=payload.description
        )

        # 建立分錄
        for entry in payload.entries:
            account = get_object_or_404(Account, id=entry.account_id)
            JournalEntry.objects.create(
                transaction=tx,
                account=account,
                amount=entry.amount,
                direction=entry.direction,
            )

    return tx


@router.get("/transactions", response=List[TransactionOut])
def list_transactions(request):
    # 使用 prefetch_related 優化 N+1 查詢問題
    return (
        Transaction.objects.all()
        .prefetch_related("entries")
        .order_by("-date", "-created_at")
    )
