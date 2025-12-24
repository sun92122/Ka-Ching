from ninja import Schema
from datetime import date
from typing import List
from decimal import Decimal


class AccountSchema(Schema):
    id: int
    code: str
    name: str
    type: str
    is_liquid: bool


class JournalEntrySchema(Schema):
    account_id: int
    amount: Decimal
    direction: str  # 'DEBIT' or 'CREDIT'


class TransactionIn(Schema):
    date: date
    description: str
    entries: List[JournalEntrySchema]


class TransactionOut(Schema):
    id: int
    date: date
    description: str
    entries: List[JournalEntrySchema]  # 會自動序列化關聯的分錄
