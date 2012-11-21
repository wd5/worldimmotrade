/**
 * jQuery Simple Slider. This Plugin add a feature slide un UL/LI
 * list with an image inside, in very simple mode. HTML Tagging required is:
 *
 * <ul>
 *   <li title="Title 1"><img title="Subtitle 1" src="image1.jpg" /></li>
 *   <li title="Title 2"><img title="Subtitle 2" src="image2.jpg" /></li>
 *   <li>...</li>
 * </ul>
 *
 * LI title and IMG title are used for show a caption on bottom of slide.
 *
 * @REL 1.1.0 you can set timeout params for each single slide.
 * Thanks to Santino Bivacqua <sanbiv@gmail.com> to suggest:
 *
 * <ul>
 *   <li rel="simpleSlider{timeOut: 4000}" title="Title 1"><img title="Subtitle 1" src="image1.jpg" /></li>
 *   <li rel="simpleSlider{timeOut: 1000}" title="Title 2"><img title="Subtitle 2" src="image2.jpg" /></li>
 *   <li>...</li>
 * </ul>
 *
 * @usage
 *
 * $('ul#myslide').simpleSlider();
 *
 * You can set some params like:
 *
 * @param 		alpha			(float)			Caption opacity (default '0.7'),
 * @param 		bgColor			(string)		Caption background color (default '#000')
 * @param		bgSpeed			(int/string)	Background image fade speed ( 'slow', 'normal', 'fast' or number of milliseconds) default 'slow'
 * @param		captionSpeed	(int/string)	Caption slideUp/slideDown speed ( 'slow', 'normal', 'fast' or number of milliseconds) default 'slow'
 * @param		height			(string)		Caption height (default '50px')
 * @param 		titleStyle		(object)		CSS Object for title ( default { color: '#fff', fontSize: '14px', fontFamily: 'Arial', margin: '0 10px 0 10px', textAlign: 'left' } )
 * @param 		subtitleStyle	(object)		CSS Object for subtitle (default { color: '#fff', fontSize: '10px', fontFamily: 'Verdana', margin: '0 10px 0 10px', textAlign: 'left' } )
 * @param		timeOut			(number)		Milliseconds interval between slide ( default 4000 )
 *
 * @sample
 *
 * $('ul#myslide').simpleSlider( {alpha: '0.5', titleStyle: { fontSize: '18px' } } );
 *
 *
 * "Simple Slider" is released under version 3.0 of the Creative Commons 
 * Attribution-Noncommercial-Share Alike license. This means that it is 
 * absolutely free for personal, noncommercial use provided that you 1)
 * make attribution to the author and 2) release any derivative work under
 * the same or a similar license.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 *
 * If you wish to use "Simple Slider" for commercial purposes, licensing information
 * can be found at http://www.undolog.com
 *
 * @author		Giovambattista Fazioli <g.fazioli@undolog.com>
 * @web			http://www.undolog.com
 * @version		1.1.6
 *
 * @changelog
 * 
 *	+ 1.1.6     Fix Safari div height size
 *	+ 1.1.5		Pacth starting fade on main start
 *	+ 1.1.0		Add rel="simpleSlider{}" attribute parameters (thanks to Santino Bivacqua <sanbiv@gmail.com>)
 *	+ 1.0.0		First release
 *
 *
 */
(function($){
	$.fn.extend( {
		simpleSlider: function(options){
			/**
			 * Set default options
			 */
			var defTitleStyle		=  { color: '#fff', fontSize: '14px', fontFamily: 'Arial', margin: '0 10px 0 10px', textAlign: 'left' };
			var defSubtitleStyle	=  { color: '#fff', fontSize: '10px', fontFamily: 'Verdana', margin: '0 10px 0 10px', textAlign: 'left' };
			var defaults = {
								alpha			: '0.7',
								bgColor			: '#000',
								bgSpeed			: 'slow',
								captionSpeed	: 'slow',
								height			: '50px',
								timeOut			: 4000,
								titleStyle		: defTitleStyle,
								subtitleStyle	: defSubtitleStyle
						   };
			/**
			 * Merge defaults options with params options
			 */
			var options = $.extend(defaults, options);
			
			return this.each(function(){
				var element = $(this);
				
				/**
				 * Get Width and Height of the first image
				 */
				var w	= element.find('img').eq(0).width();
				var h	= element.find('img').eq(0).height();
				
				/**
				 * Margin for show caption
				 */
				var ms	=  '-'+options.height;
				
				/**
				 * half size of caption
				 */
				var hsc	= String( parseInt( options.height ) / 2 )+'px';
				
				/**
				 * List of all slide
				 */
				var items	= [];
				var index	= 0;
				
				/**
				 * get speed
				 */
				var bgSpeed			= isNaN( parseInt( options.bgSpeed ) ) ? options.bgSpeed : parseInt( options.bgSpeed );
				var captionSpeed	= isNaN( parseInt( options.captionSpeed ) ) ? options.captionSpeed : parseInt( options.captionSpeed );
				
				var start = function() {
					var timeOut = ( $(items[ index ]).data('timeOut') == undefined ) ? parseInt( options.timeOut ) : $(items[ index ]).data('timeOut');
					$( items[ index ] ).children('div').animate( { marginTop: ms }, captionSpeed, function() { setTimeout( nextItem, timeOut ); } );					
				};
				
				var loopItem	= function() {
					$( items[ index ] ).fadeIn( bgSpeed, start );
				};
				
				var nextItem	= function() {
					$( items[ index ] ).children('div').animate( { marginTop: '0' }, captionSpeed, function() { $(this).parent().fadeOut( bgSpeed, loopItem ); } );
					index++; if( index > ( items.length-1) ) index = 0;
				};
				
				/**
				 * Avoid ul standard style
				 */
				element.css( { 
							listStyle	: 'none',
							padding		: '0px',
							width		: w+'px',
							height		: h+'px',
							overflow	: 'hidden'
						  } )
					.children('li')
					.css( {	
							margin		: '0', 
							display		: 'block',
							width		: w+'px',
							height		: h+'px',
							overflow	: 'hidden'
						  } )
					.append( '<div><h1></h1><p><p></div>' )
					.children('div')
					.css({ 
							position		: 'relative',
							backgroundColor	: options.bgColor,
							opacity			: options.alpha,
							width			: w+'px',
							height			: options.height+'px',
							overflow		: 'hidden'
						 });
						 
				element.find('li')
					.each(
						function(i,e) {
							/**
							 * + Add $Rel.1.1.0
							 * Check rel attribute for custom timeout in each single slide
							 */
							var r = $(this).attr('rel');
							if( r != undefined ) {
								if( r.indexOf( 'simpleSlider' ) != -1 ) {
									eval ( 'var o = ' + ( r.substr( r.indexOf( '{' ), ( r.length - 1 ) ) ) );
									$(e).data ( 'timeOut', o.timeOut );
								}
							}
							 
							var t = $(this).attr('title');
							var s = $(this).find('img').eq(0).attr('title');
							// collection
							items[ i ]	= e;
							if(i>0) $(e).hide();

							$(this).find('h1')
								.css( defTitleStyle )
								.css( options.titleStyle )
								.html( t )
								.next('p')
								.css( defSubtitleStyle )
								.css( options.subtitleStyle )
								.html( s );
						}
					);
				start();	// play the game						 
			});
		}
	});
})(jQuery);