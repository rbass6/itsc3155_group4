import pytest
from Invoice import Invoice


@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice

def test_CanCalculateTotalImpurePrice(invoice, products):
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75

def test_CanCalucateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62

def test_CanCalucateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

#tests if the add product function works by looking at
# total price and making sure the numbers are correct
def test_canAddProduct(invoice, products):

        result = Invoice().addProduct(1, 2, 3)
        products["test"]= result

        invoice.totalImpurePrice(products)
        assert invoice.totalImpurePrice(products) == 77

# makes sure the discount function works after the add function has been run
def test_correctTotalDiscountAfterAdd(invoice, products):
    result = Invoice().addProduct(1, 2, 3)
    products["test"] = result

    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.68