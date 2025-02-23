# accuknox_assignment/signals.py

import time
import threading
from django.db import transaction
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# ----------------------------
# Q1: Synchronous Execution Demonstration
# ----------------------------
@receiver(post_save, sender=User, dispatch_uid="sync_signal_handler")
def sync_signal_handler(sender, instance, **kwargs):
    print(f"[Q1] Signal handler executing in thread: {threading.current_thread().name}")
    print("[Q1] Signal execution started (sleeping for 3 seconds)...")
    time.sleep(3)  # Simulate work/delay
    print("[Q1] Signal execution finished.")

def test_sync_signal():
    """Test that signals execute synchronously."""
    print(f"[Q1] Caller thread: {threading.current_thread().name}")
    user = User.objects.create(username="sync_test_user")
    print("[Q1] User created; signal should have already finished.")

# ----------------------------
# Q2: Same Thread Demonstration
# ----------------------------
@receiver(post_save, sender=User, dispatch_uid="thread_signal_handler")
def thread_signal_handler(sender, instance, **kwargs):
    print(f"[Q2] Inside signal handler. Thread: {threading.current_thread().name}")

def test_thread_signal():
    """Test that signals run in the same thread as the caller."""
    print(f"[Q2] Caller thread: {threading.current_thread().name}")
    user = User.objects.create(username="thread_test_user")

# ----------------------------
# Q3: Database Transaction Demonstration
# ----------------------------
@receiver(post_save, sender=User, dispatch_uid="transaction_signal_handler")
def transaction_signal_handler(sender, instance, **kwargs):
    print("[Q3] Signal handler executed (post_save).")

def test_transaction_signal():
    """Test signal behavior inside a transaction."""
    print("[Q3] Starting transaction...")
    with transaction.atomic():
        user = User.objects.create(username="transaction_test_user")
        print("[Q3] User created inside transaction (but not yet committed).")
    print("[Q3] Transaction committed!")
