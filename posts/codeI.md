title: Code highlight test
subtitle: Gimme some colors
date: 2015-10-15


# Code Highlight test

	:::javascript
	var logger = bucker.createLogger({
	    file: {
	        filename: '../../log.log',
	        format: ':level :time :data',
	        timestamp: 'HH:mm:ss',
	        accessFormat: ':time :level :method :status :url'
	    },
	    console: {
	        color: true
	    },
	    name: 'quantum'
	});
