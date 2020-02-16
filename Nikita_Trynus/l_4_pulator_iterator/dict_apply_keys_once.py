from collections import UserDict


class GreedyDict(UserDict, dict):
    def __setitem__(self, key, value):
        if key in self.__dict__['data'].keys():
            raise AttributeError('Keys could be applied only once')
        else:
            super().__setitem__(key, value)

    def update(self, dict_to_record):
        """add a key from dict_to_record
            that match keys in origin to dict with name 'key_1' """
        for key, value in dict_to_record.items():
            if key in self.__dict__['data'].keys():
                self[f'{key}_1'] = value

    def pop(self, dict_to_pop):
        """pop all keys from dict_to_record
            that match keys in origin to dict  """
        for key, value in dict_to_pop.items():
            if key in self.__dict__['data'].keys():
                super().pop(key)

    def copy(self):
        return dict(self.__dict__['data'])
