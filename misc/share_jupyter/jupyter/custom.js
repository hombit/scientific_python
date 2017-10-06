define([
    'base/js/namespace',
    'base/js/events'
    ],
    function(IPython, events) {
        events.on("notebook_loaded.Notebook",
        	function () {
  				IPython.notebook.set_autosave_interval(2000); //in milliseconds
			}
  		);
    }
);
