# class NoLenSupport:
#     pass
#
# obj = NoLenSupport()
# len(obj)


class LenSupport:
    def __len__(self):
        return 42


obj = LenSupport()
len(obj)
# 42
