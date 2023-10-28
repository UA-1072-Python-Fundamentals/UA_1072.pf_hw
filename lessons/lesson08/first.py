print("first -> ", __name__)

__all__ = ["a", "__c"]
a = 1
_b = 2
__c = 3
d = 4

if __name__ == "__main__":
    print("entry point is first")
