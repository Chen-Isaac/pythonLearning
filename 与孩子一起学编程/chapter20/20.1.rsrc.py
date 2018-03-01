{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgTemplate',
          'title':'Standard Template with File->Exit menu',
          'size':(400, 300),
          'style':['resizeable'],

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':'E&xit',
                   'command':'exit',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'Button', 
    'name':'replay', 
    'position':(280, 105), 
    'label':u'confirmReplay', 
    },

{'type':'StaticText', 
    'name':'StaticText3', 
    'position':(17, 72), 
    'text':u"What's yer guess?", 
    },

{'type':'TextField', 
    'name':'result', 
    'position':(20, 142), 
    'size':(315, 70), 
    },

{'type':'Button', 
    'name':'cofBtn', 
    'position':(165, 106), 
    'label':u'confirmButton', 
    },

{'type':'Spinner', 
    'name':'guessNum', 
    'position':(18, 106), 
    'max':100, 
    'min':0, 
    'value':3, 
    },

{'type':'StaticText', 
    'name':'StaticText2', 
    'position':(17, 41), 
    'text':u"It is a number from 1 to 99. I'll give you 6 tries.", 
    },

{'type':'StaticText', 
    'name':'StaticText1', 
    'position':(16, 17), 
    'text':u"AHOY! I'm the Dread Pirate Roberts, and I have a secret!", 
    },

] # end components
} # end background
] # end backgrounds
} }
