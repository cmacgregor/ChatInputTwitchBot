
from virtualcontroller import VirtualController


class DarksoulsVirtualController(VirtualController):
    def __init__(self, virtualGamepad):
        super().__init__(self, virtualGamepad)

    actions ={
        #interaction synonyms
        'INTERACT',
        'PICKUP',
        'CLIMB',
        #evasive manuvers
        'ROLL',
        'ROLL FORWARD',
        'ROLL BACK',
        'ROLL LEFT',
        'ROLL RIGHT',
        'ROLL FORWARD LEFT',
        'ROLL FORWARD RIGHT',
        'ROLL BACK LEFT',
        'ROLL BACK RIGHT',
        'BACKSTEP'
        #attacks 
        'LIGHT RIGHT',
        'HEAVY RIGHT',
        'LIGHT LEFT',
        'HEAVY LEFT',
        #simple actions
        'ITEM',
        'TOGGLE TWO HAND',
        'CYCLE SPELL',
        'CYCLE ITEM',
        'CYCLE LEFT HAND',
        'CYCLE RIGHT HAND',
        'FIRST SPELL',
        'FIRST ITEM',
        'FIRST LEFT HAND',
        'FIRST RIGHT HAND',  
    },
    movement = {
        'MOVE FORWARD',
        'MOVE BACK',
        'MOVE LEFT',
        'MOVE RIGHT',
        'MOVE FORWARD LEFT',
        'MOVE FORWARD RIGHT',
        'MOVE BACK LEFT',
        'MOVE BACK RIGHT',
        'FACE FORWARD',
        'FACE BACK',
        'FACE LEFT',
        'FACE RIGHT',
        'FACE FORWARD LEFT',
        'FACE FORWARD RIGHT',
        'FACE BACK LEFT',
        'FACE BACK RIGHT',
        'JUMP',
        'JUMP ROLL'
    }
    camera = {
        'TARGET ENEMY',
        'CAMERA CENTER',
        'CAMERA UP',
        'CAMERA DOWN',
        'CAMERA LEFT',
        'CAMERA RIGHT',
        'CAMERA FORWARD LEFT',
        'CAMERA UP LEFT',
        'CAMERA UP RIGHT',
        'CAMERA DOWN LEFT',
        'CAMERA DOWN RIGHT',
    }

    VirtualController.valid_inputs = actions + movement + camera