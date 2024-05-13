from gdo.base.GDO_Module import GDO_Module
from gdo.gpg.GDO_GPG import GDO_GPG


class module_gpg(GDO_Module):

    def gdo_classes(self):
        return [
            GDO_GPG,
        ]

