from datetime import date, timedelta
import pytest
from model import Batch, OrderLine

def test_allocating_to_a_batch_reduces_the_available_quantity():
    batch = Batch ('batch-001', 'SMALL-TABLE', qty=20, eta=date.today())
    line = OrderLine('order-ref', 'SMALL-TABLE', 2)
    batch.allocate(line)
    assert batch.available_quantity == 18

def test_can_allocate_if_available_greater_than_required():
    '''
    arrange: создать батч на 20 экземпляров и товарную позицию на 19 экземпляров
    act: запросить метод can_allocate
    assert: убедиться, что метод отдал истину
    '''
    pytest.fail("todo")


def test_cannot_allocate_if_available_smaller_than_required():
    '''
    arrange: создать батч на 20 экземпляров и товарную позицию на 21 экземпляров
    act: запросить метод can_allocate
    assert: убедиться, что метод отдал ложь
    '''
    pytest.fail("todo")


def test_can_allocate_if_available_equal_to_required():
    '''
    arrange: создать батч на 20 экземпляров и товарную позицию на 20 экземпляров
    act: запросить метод can_allocate
    assert: убедиться, что метод отдал истину
    '''
    pytest.fail("todo")

@pytest.mark.skip()
def test_cannot_allocate_if_skus_do_not_match():
    batch = Batch("batch-001", "UNCOMFORTABLE-CHAIR", 100, eta=None)
    different_sku_line = OrderLine("order-123", "EXPENSIVE-TOASTER", 10)
    assert batch.can_allocate(different_sku_line) is False

@pytest.mark.skip()
def test_allocation_is_idempotent():
    batch, line = make_batch_and_line("ANGULAR-DESK", 20, 2)
    batch.allocate(line)
    batch.allocate(line)
    assert batch.available_quantity == 18

@pytest.mark.skip()
def test_deallocate():
    batch, line = make_batch_and_line("EXPENSIVE-FOOTSTOOL", 20, 2)
    batch.allocate(line)
    batch.deallocate(line)
    assert batch.available_quantity == 20

@pytest.mark.skip()
def test_can_only_deallocate_allocated_lines():
    batch, unallocated_line = make_batch_and_line("DECORATIVE-TRINKET", 20, 2)
    batch.deallocate(unallocated_line)
    assert batch.available_quantity == 20