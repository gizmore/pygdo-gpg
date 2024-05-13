from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_Text import GDT_Text
from gdo.core.GDT_User import GDT_User
from gdo.date.GDT_Created import GDT_Created
from gdo.gpg.GDT_GPGPublicKey import GDT_GPGPublicKey


class GDO_GPG(GDO):

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_User('gpg_uid').primary(),
            GDT_GPGPublicKey('gpg_pubkey').not_null(),
            GDT_Text('gpg_key_encrypted'),
            GDT_Created('gpg_created'),
        ]
