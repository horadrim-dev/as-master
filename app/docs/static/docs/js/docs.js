(function($) {

    // var original_onPageLoad = $.fn.onPageLoad;
    // $.fn.onPageLoad = function () {
    //     original_onPageLoad();

        $('#docs-filter input.autoapply').on('change', function() {
            $(this).closest("form").submit();
            
        });
        $('#docs-filter input#filter-reset').on('click', function() {
            $(this).closest("form").reset();
            //$(this).closest("form").find('input:not([type="submit"])').val('');
        });

    // };
})(jQuery || django.jQuery);
