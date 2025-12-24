from django.contrib import admin
from .models import Account, Transaction, JournalEntry


# 讓交易介面可以直接編輯分錄 (Inline)
class JournalEntryInline(admin.TabularInline):
    model = JournalEntry
    extra = 2  # 預設顯示兩行 (一借一貸)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("date", "description", "total_amount", "created_at")
    inlines = [JournalEntryInline]
    date_hierarchy = "date"


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "type", "is_liquid")
    list_filter = ("type", "is_liquid")
    search_fields = ("code", "name")
