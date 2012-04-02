/**
 * Plone snippet Plugin
 *
 * @author Maurizio Lupo
 */

(function() {
    tinymce.PluginManager.requireLangPack('snippet');
    tinymce.create('tinymce.plugins.SnippetPlugin', {
        init : function(ed, url) {
            // Register commands
            ed.addCommand('mceSnippet', function() {

                ed.windowManager.open({
                    file : url + '/dialog.htm',
                    width :  parseInt(ed.getParam("paste_dialog_width", "450")),
                    height :  parseInt(ed.getParam("paste_dialog_height", "400")),
                    inline : 1
                }/*, {
                    plugin_url : url, // Plugin absolute URL
					some_custom_arg : 'custom arg' // Custom argument
                }*/);
            });

            // Register buttons
            ed.addButton('snippet', {
                title : 'snippet.desc',
                cmd : 'mceSnippet',
                image : url + '/img/snippet.gif'
            });
            
        },
        
         /**
		 * Creates control instances based in the incomming name. This method is normally not
		 * needed since the addButton method of the tinymce.Editor class is a more easy way of adding buttons
		 * but you sometimes need to create more complex controls like listboxes, split buttons etc then this
		 * method can be used to create those.
		 *
		 * @param {String} n Name of the control to create.
		 * @param {tinymce.ControlManager} cm Control manager to use inorder to create new control.
		 * @return {tinymce.ui.Control} New control instance or null if no control was created.
		 */
//		 
//		 createControl : function(n, cm) {
//			return null;
//		},

		/**
		 * Returns information about the plugin as a name/value array.
		 * The current keys are longname, author, authorurl, infourl and version.
		 *
		 * @return {Object} Name/value array containing information about the plugin.
		 */

        getInfo : function() {
            return {
                longname : 'Snippet Plugin',
                author : 'Maurizio Lupo',
                authorurl : 'http://redomino.com',
                infourl : 'http://plone.org/products/tinymce',
                version : "0.1"
            };
        }
    });

    // Register plugin
    tinymce.PluginManager.add('snippet', tinymce.plugins.SnippetPlugin);
})();
