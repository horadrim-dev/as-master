(function($) {

    // var original_onPageLoad = $.fn.onPageLoad;
    // $.fn.onPageLoad = function () {
    //     original_onPageLoad();

    $(document).ready(function(){
        
        $('.animated-numbers').each(function(){

        var self = $(this);

        $(this).waypoint(function( direction ) {
            if( direction === 'down' && !$(this.element).hasClass('ftco-animated') ) {
                var comma_separator_number_step = $.animateNumber.numberStepFactories.separator(',')
                $('.number').each(function(){
                var $this = $(this),
                    num = $this.data('number');
                $this.animateNumber(
                    {
                    number: num,
                    numberStep: comma_separator_number_step
                    }, $this.data('speed')
                );
                });
            }
            } , { offset: '95%' }
        );
        });

	});

})(jQuery);
