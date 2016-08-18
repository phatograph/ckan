import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


def create_country_codes():
    user = toolkit.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    try:
        data = {'id': 'country_codes'}
        toolkit.get_action('vocabulary_show')(context, data)
    except toolkit.ObjectNotFound:
        data = {'name': 'country_codes'}
        vocab = toolkit.get_action('vocabulary_create')(context, data)
        for tag in (u'uk', u'ie', u'de', u'fr', u'es'):
            data = {'name': tag, 'vocabulary_id': vocab['id']}
            toolkit.get_action('tag_create')(context, data)

def country_codes():
    create_country_codes()
    try:
       tag_list = toolkit.get_action('tag_list')
       country_codes = tag_list(data_dict={'vocabulary_id': 'country_codes'})
       return country_codes
    except toolkit.ObjectNotFound:
       return None
##create the keywords set
#def create_country_codes():
def create_keywords_set():
    user = toolkit.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    try:
        ##data = {'id': 'country_codes'}
        data = {'id': 'keywords_set'}
        toolkit.get_action('vocabulary_show')(context, data)
    except toolkit.ObjectNotFound:
        data = {'name': 'keywords_set'}
        vocab = toolkit.get_action('vocabulary_create')(context, data)
        for tag in (u'802.11', u'802.11 frames', u'802.11 a', u'802.11 b', u'802.11 g', u'802.15', u'802.11 g', u'802.15.4', u'802.16', u'Bluetooth', u'DTN', u'GPS', u'MANET', u'RFMON', u'ORBIT', u'SNMP', u'802.11 g', u'authentication log', u'cellular network', u'Wi-Fi hotspot', u'location', u'packet trace', u'sensor network', u'signal strength', u'social network', u'syslog', u'tcpdump', u'vehicular network', u'wardriving', u'wireless mesh network', u'RFID', u'wireless multihop networks', u'None of the above',):
                data = {'name': tag, 'vocabulary_id': vocab['id']}
                toolkit.get_action('tag_create')(context, data)

def keywords_set():
    create_keywords_set()
    try:
       tag_list = toolkit.get_action('tag_list')
       keywords_set = tag_list(data_dict={'vocabulary_id': 'keywords_set'})
       return keywords_set
    except toolkit.ObjectNotFound:
       return None



class ExampleIDatasetFormPlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IDatasetForm)
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    ##def create_package_schema(self):
        # let's grab the default schema in our plugin
       ## schema = super(ExampleIDatasetFormPlugin, self).create_package_schema()
                        #our custom field
        ##schema.update({
          ##  'custom_text': [toolkit.get_validator('ignore_missing'),
         ##                   toolkit.get_converter('convert_to_extras')]
       ## })
        ##return schema
    ##def update_package_schema(self):
        ##schema = super(ExampleIDatasetFormPlugin, self).update_package_schema()
                    #our custom field
        ##schema.update({
          ##  'custom_text': [toolkit.get_validator('ignore_missing'),
##                            toolkit.get_converter('convert_to_extras')]
        ##})
        ##return schema
    def _modify_package_schema(self, schema):
        # Add our custom country_code metadata field to the schema.
        schema.update({
            'country_code': [toolkit.get_validator('ignore_missing'),
                                 toolkit.get_converter('convert_to_tags')('country_codes')]
        })

        schema.update({
            'oneline':     [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'releasedate': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'menddate': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'journaldoi': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'journalbibtex': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            #'ris': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            #'keyword': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            #'journaldoi': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'measpurposes': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'networktype': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'environment': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'network': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'collection': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'sanitization': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'hole': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'error': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'limitation': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'note': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'datasetbibtex': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'datasetris': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')]
            #'license': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')]
        })
        # schema.update({
        #     'releasedate': [toolkit.get_validator('ignore_missing'),
        #                         toolkit.get_converter('convert_to_extras')]
        # })
        # schema.update({
        #     'menddate': [toolkit.get_validator('ignore_missing'),
        #                      toolkit.get_converter('convert_to_extras')]
        # })
        # schema.update({
        #     'references': [toolkit.get_validator('ignore_missing'),
        #                        toolkit.get_converter('convert_to_extras')]
        # })
        # schema.update({
        #     'keyword': [toolkit.get_validator('ignore_missing'),
        #                     toolkit.get_converter('convert_to_extras')]
        # })
        # schema.update({
        #     'measpurposes': [toolkit.get_validator('ignore_missing'),
        #                          toolkit.get_converter('convert_to_extras')] 
        # })
        # schema.update({
        #     'networktype': [toolkit.get_validator('ignore_missing'),
        #                          toolkit.get_converter('convert_to_extras')]
        # })
        # schema.update({
        #     'environment': [toolkit.get_validator('ignore_missing'),
        #                        toolkit.get_converter('convert_to_extras')]
        # })
        # schema.update({
        #     'network': [toolkit.get_validator('ignore_missing'),
        #                     toolkit.get_converter('convert_to_extras')]
        # })
        # schema.update({
        #     'collection': [toolkit.get_validator('ignore_missing'),
        #                        toolkit.get_converter('convert_to_extras')]
        # })
        # schema.update({
        #     'sanitization': [toolkit.get_validator('ignore_missing'),
        #                          toolkit.get_converter('convert_to_extras')]
        # })
        # schema.update({
        #     'hole': [toolkit.get_validator('ignore_missing'),
        #                  toolkit.get_converter('convert_to_extras')]
        # })
        # schema.update({
        #     'error': [toolkit.get_validator('ignore_missing'),
        #                   toolkit.get_converter('convert_to_extras')]
        # })
        # schema.update({
        #     'limitation': [toolkit.get_validator('ignore_missing'),
        #                        toolkit.get_converter('convert_to_extras')]
        # })
        # schema.update({
        #     'note': [toolkit.get_validator('ignore_missing'),
        #                  toolkit.get_converter('convert_to_extras')]
        # })
               ##schema.update({
          ##  'country_code': [
            ##    toolkit.get_validator('ignore_missing'),
              ##  toolkit.get_converter('convert_to_tags')('country_codes')]
       ## })
        # Add our custom_resource_text metadata field to the schema
        schema['resources'].update({
               'custom_resource_text' : [ toolkit.get_validator('ignore_missing') ]
               })
       # schema.update({
       #     'keyword_set': [
       #            toolkit.get_validator('ignore_missing'),
       #            toolkit.get_converter('convert_to_tags')('keywords_set')
       #     ]
       # })
        return schema

    def create_package_schema(self):
        schema = super(ExampleIDatasetFormPlugin, self).create_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def update_package_schema(self):
        schema = super(ExampleIDatasetFormPlugin, self).update_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def show_package_schema(self):
        schema = super(ExampleIDatasetFormPlugin, self).show_package_schema()

        # Don't show vocab tags mixed in with normal 'free' tags
                # (e.g. on dataset pages, or on the search page)
        schema['tags']['__extras'].append(toolkit.get_converter('free_tags_only'))

                                # Add our custom country_code metadata field to the schema.
       # schema.update({
       #     'country_code': [
       #         tk.get_converter('convert_from_tags')('country_codes'),
       #         tk.get_validator('ignore_missing')]
       #     })
        schema.update({
            'oneline': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
            'releasedate': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
            'menddate': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
            'journaldoi': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
            'journalbibtex': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
            #'ris': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
            #'keyword': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
            #'journaldoi': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
            'measpurposes': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
            'networktype': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
            #'measpurposes': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
            #'networktype': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
            'environment': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
            'network': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
            'collection': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
            'sanitization': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
            'hole': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
            'error': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
            'limitation': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
            'note': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
            'datasetbibtex': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
            'datasetris': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')]
            #'license': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')]
        })
       # schema.update({
       #     'releasedate': [toolkit.get_converter('convert_from_extras'),
       #                         toolkit.get_validator('ignore_missing')]
       # })
       # schema.update({
       #     'menddate': [toolkit.get_converter('convert_from_extras'),
       #                      toolkit.get_validator('ignore_missing')]
       # })
       # schema.update({
       #     'references': [toolkit.get_converter('convert_from_extras'),
       #                        toolkit.get_validator('ignore_missing')]
       # })
       # schema.update({
       #     'keyword': [toolkit.get_converter('convert_from_extras'),
       #                     toolkit.get_validator('ignore_missing')]
       # })
       # schema.update({
       #     'environment': [toolkit.get_converter('convert_from_extras'),
       #                        toolkit.get_validator('ignore_missing')]
       # })
       # schema.update({
       #     'network': [toolkit.get_converter('convert_from_extras'),
       #                     toolkit.get_validator('ignore_missing')]
       # })
       # schema.update({
       #     'collection': [toolkit.get_converter('convert_from_extras'),
       #                        toolkit.get_validator('ignore_missing')]
       # })
       # schema.update({
       #     'sanitization': [toolkit.get_converter('convert_from_extras'),
       #                          toolkit.get_validator('ignore_missing')]
       # })
       # schema.update({
       #     'hole': [toolkit.get_converter('convert_from_extras'),
       #                  toolkit.get_validator('ignore_missing')]
       # })
       # schema.update({
       #     'error': [toolkit.get_converter('convert_from_extras'),
       #                   toolkit.get_validator('ignore_missing')]
       # })
       # schema.update({
       #     'limitation': [toolkit.get_converter('convert_from_extras'),
       #                        toolkit.get_validator('ignore_missing')]
       # })
       # schema.update({
       #     'note': [toolkit.get_converter('convert_from_extras'),
       #                  toolkit.get_validator('ignore_missing')]
       # })
# Don't show vocab tags mixed in with normal 'free' tags
                # (e.g. on dataset pages, or on the search page)
        ##schema['tags']['__extras'].append(toolkit.get_converter('free_tags_only'))
        # Add our custom country_code metadata field to the schema.
        ##schema.update({

            ##'country_code': [
              ##  toolkit.get_converter('convert_from_tags')('country_codes'),
            ##    toolkit.get_validator('ignore_missing')]
          ##  })
       # schema['resources'].update({
       #         'custom_resource_text' : [ toolkit.get_validator('ignore_missing') ]
        #    })
        #schema['tags']['__extras'].append(toolkit.get_converter('free_tags_only'))
       # schema.update({
        #    'keyword_set': [
         #         toolkit.get_converter('convert_from_tags')('keywords_set'),
          #        toolkit.get_validator('ignore_missing')]
           # })
        return schema

    def is_fallback(self):
            # Return True to register this plugin as the default handler for
                    # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
                                        # This plugin doesn't handle any special package types, it just
                                                # registers itself as the default (above).
        return []
    def update_config(self, config):
          # Add this plugin's templates dir to CKAN's extra_template_paths, so
                  # that CKAN will use this plugin's custom templates.
        toolkit.add_template_directory(config, 'templates')

    def get_helpers(self):
        return {'country_codes': country_codes}

class ExtrafieldsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'extrafields')
