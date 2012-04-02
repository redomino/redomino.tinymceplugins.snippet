from Products.CMFCore.utils import getToolByName

class SetupVarious:

    def __call__(self, context):

        # Ordinarily, GenericSetup handlers check for the existence of XML files.
        # Here, we are not parsing an XML file, but we use this text file as a 
        # flag to check that we actually meant for this import step to be run.
        # The file is found in profiles/default.

        if context.readDataFile('redomino.tinymceplugins.snippet_various.txt') is None:
            return

        # Add additional setup code here
        site = context.getSite()
        self.setupTransforms(site)
        #self.setup_filter_html(site)

    def setupTransforms(portal, out):
        from Products.CMFDefault.utils import VALID_TAGS
        from Products.CMFDefault.utils import NASTY_TAGS

        valid_tags = VALID_TAGS.copy()
        nasty_tags = NASTY_TAGS.copy()

        nasty_tags.pop('embed')
        nasty_tags.pop('object')

        valid_tags['embed'] = 1
        valid_tags['object'] = 1
        valid_tags['iframe'] = 1

        kwargs = {'nasty_tags': nasty_tags,
                  'valid_tags': valid_tags}
    
        transform = getattr(getToolByName(portal, 'portal_transforms'), 'safe_html')

        for k in list(kwargs):
            if isinstance(kwargs[k], dict):
                v = kwargs[k]
                kwargs[k+'_key'] = v.keys()
                kwargs[k+'_value'] = [str(s) for s in v.values()]
                del kwargs[k]

        transform.set_parameters(**kwargs)
        transform.reloadTransforms()


def setupVarious(context):
    """ setup various step. Handles for steps not handled by a gs profile """
    handler = SetupVarious()
    handler(context)
