from django.db import models
from django.utils.translation import gettext_lazy as _


# --- 1. 系統全域設定 (修復 Nginx Init 錯誤所需) ---
class SystemSetting(models.Model):
    """
    全域設定表 (Singleton 模式，永遠只取 ID=1)
    """

    company_name = models.CharField(max_length=100, default="我的公司")
    lock_date = models.DateField(null=True, blank=True, help_text="關帳日")
    enable_budget_workflow = models.BooleanField(
        default=False, help_text="啟用預決算簽核流程"
    )
    default_approval_config = models.JSONField(
        default=dict, blank=True, help_text="預設簽核流程設定"
    )
    allowed_domains = models.JSONField(default=list, help_text="允許訪問的網域名稱")

    def save(self, *args, **kwargs):
        self.pk = 1  # 強制 ID 為 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    class Meta:
        verbose_name = "系統設定"
        verbose_name_plural = "系統設定"


# --- 2. 會計基礎資料 ---
class Account(models.Model):
    class Type(models.TextChoices):
        ASSET = "ASSET", _("資產")
        LIABILITY = "LIABILITY", _("負債")
        EQUITY = "EQUITY", _("權益")
        INCOME = "INCOME", _("收入")
        EXPENSE = "EXPENSE", _("支出")

    code = models.CharField(max_length=20, unique=True, help_text="科目代碼")
    name = models.CharField(max_length=100, help_text="科目名稱")
    type = models.CharField(max_length=10, choices=Type.choices)
    is_liquid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.code} {self.name}"


# --- 3. 交易核心 ---
class Transaction(models.Model):
    """交易主檔"""

    date = models.DateField(help_text="交易日期")
    description = models.CharField(max_length=255, help_text="摘要")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.date} - {self.description}"

    @property
    def total_amount(self):
        return (
            self.entries.filter(direction="DEBIT").aggregate(models.Sum("amount"))[
                "amount__sum"
            ]
            or 0
        )


class JournalEntry(models.Model):
    """交易分錄"""

    class Direction(models.TextChoices):
        DEBIT = "DEBIT", _("借")
        CREDIT = "CREDIT", _("貸")

    transaction = models.ForeignKey(
        Transaction, related_name="entries", on_delete=models.CASCADE
    )
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    direction = models.CharField(max_length=6, choices=Direction.choices)

    def __str__(self):
        return f"{self.transaction} - {self.account} ({self.direction} {self.amount})"
