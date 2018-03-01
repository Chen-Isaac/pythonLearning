{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgTemplate',
          'title':'Standard Template with File->Exit menu',
          'size':(563, 300),
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
             {'type':'Menu',
             'name':'menuConvert',
             'label':u'&Convert',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuConvertCtoF',
                   'label':u'&Celsius to Fahrenheit',
                  },
                  {'type':'MenuItem',
                   'name':'menuConvertFtoC',
                   'label':u'&Fahrenheit to Celsius',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'StaticText', 
    'name':'StaticText2', 
    'position':(389, 124), 
    'text':u'Fahrenheit', 
    },

{'type':'StaticText', 
    'name':'StaticText1', 
    'position':(34, 118), 
    'text':u'Celsius', 
    },

{'type':'Spinner', 
    'name':'spinFahr', 
    'position':(385, 78), 
    'max':500, 
    'min':-500, 
    'value':0, 
    },

{'type':'Button', 
    'name':'btnFtoC', 
    'position':(187, 121), 
    'label':u'<<<Fahrenheit to Celsius', 
    },

{'type':'Button', 
    'name':'btnCtoF', 
    'position':(185, 78), 
    'size':(161, -1), 
    'label':u'Celsius to Fahrenheit>>>', 
    },

{'type':'TextField', 
    'name':'tfCel', 
    'position':(32, 83), 
    },

] # end components
} # end background
] # end backgrounds
} }
