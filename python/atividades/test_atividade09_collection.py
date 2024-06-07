import pytest
from atividade09_collection import Item, ItemCollection

def test_add_item_with_valid_item():
    collection = ItemCollection()
    item = Item("Item 1")
    collection.add_item(item)
    assert len(collection.get_items()) == 1
    assert item in collection.get_items()

def test_add_item_with_invalid_item():
    collection = ItemCollection()
    with pytest.raises(ValueError, match="Item must be a valid Item instance"):
        collection.add_item(None)

def test_remove_existing_item():
    collection = ItemCollection()
    item = Item("Item 1")
    collection.add_item(item)
    collection.remove_item(item)
    assert len(collection.get_items()) == 0

def test_remove_non_existing_item():
    collection = ItemCollection()
    item = Item("Item 1")
    with pytest.raises(ValueError, match="Item not found in the collection"):
        collection.remove_item(item)

def test_get_items():
    collection = ItemCollection()
    item1 = Item("Item 1")
    item2 = Item("Item 2")
    collection.add_item(item1)
    collection.add_item(item2)
    assert collection.get_items() == [item1, item2]

if __name__ == "__main__":
    pytest.main(["-s","-x","test_atividade09_collection.py","-vv"])
