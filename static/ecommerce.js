$(document).ready(function (){
    //Contact Form
    var contactForm = $('.contact-form')
    var contactFormMethod = contactForm.attr('method')
    var contactFormEndpoint = contactForm.attr('action')

    function contactSubmitting(isSubmit, text, submitBtn){
        if(isSubmit){
            submitBtn.addClass('disabled');
            submitBtn.html("<i class=\"fa fa-spinner fa-spin\"></i> Sending...");
        } else {
            submitBtn.removeClass('disabled');
            submitBtn.html(text);
        }
    }

    contactForm.submit(function (event){
        event.preventDefault();

        var contactFormSubmitBtn = contactForm.find("[type='submit']")
        var contactFormSubmitBtnTxt = contactFormSubmitBtn.text()

        var contactFormData = contactForm.serialize()
        var thisForm = $(this)

        contactSubmitting(true, "", contactFormSubmitBtn)

        $.ajax({
            method: contactFormMethod,
            url: contactFormEndpoint,
            data: contactFormData,
            success: function (data){
                contactForm[0].reset()
                $.alert({
                    title: 'Success!',
                    content: data.message,
                    theme: 'modern',
                })
                setTimeout(function (){
                    contactSubmitting(false, contactFormSubmitBtnTxt, contactFormSubmitBtn)
                }, 1000)
            },
            error: function (errorData){
                var jsonData = errorData.responseJSON
                var msg = ''

                $.each(jsonData, function(key, value){
                    msg += key + ": " + value[0].message + '<br/>'
                })
                $.alert({
                    title: 'Opps!',
                    content: msg,
                    theme: 'modern',
                })
                setTimeout(function (){
                    contactSubmitting(false, contactFormSubmitBtnTxt, contactFormSubmitBtn)
                }, 1000)
            },
        })
    })

    // Auto Search
    var searchForm = $('.search-form')
    var searchInput = searchForm.find('[name="q"]')
    var typingTimer;
    var typingIntervel = 1500;
    var searchBtn = searchForm.find('[type="submit"]')

    searchInput.keyup(function (event){
        clearTimeout(typingTimer);
        typingTimer = setTimeout(perfomSearch, typingIntervel);
    })

    searchInput.keydown(function (event){
        clearTimeout(typingTimer);
    })

    function doingSearch(){
        searchBtn.addClass('disabled');
        searchBtn.html("<i class=\"fa fa-spinner fa-spin\"></i> Searching");
    }

    function perfomSearch(){
        doingSearch()
        var query = searchInput.val();
        setTimeout(function (){
            window.location.href = '/search/?q=' + query;
        }, 1000);
    }


    // Cart + Add Products
    var productForm = $('.product-ajax')
    productForm.submit(function (event){
        event.preventDefault();
        var thisForm = $(this)
        // var actionEndPoint = thisForm.attr('action');
        var actionEndPoint = thisForm.attr('data-endpoint');
        var httpMethod = thisForm.attr('method');
        var formData = thisForm.serialize();

        $.ajax({
            url: actionEndPoint,
            method: httpMethod,
            data: formData,
            success: function (data){
                var submitSpan = thisForm.find('.submit-span')
                if(data.added){
                    submitSpan.html('In cart <button type="submit" class=\'btn btn-link\'>Remove?</button>')
                }else{
                    submitSpan.html('<button type="submit" class=\'btn btn-success\'>Add to cart</button>')
                }
                var navbarCount = $('.navbar-cart-count')
                navbarCount.text(data.cartItemCount)
                var currentPath = window.location.href
                if(currentPath.indexOf('cart') !== -1){
                    refreshCart()
                }
            },
            error: function (errorData){
                $.alert({
                    title: 'Opps!',
                    content: 'An Error occurred',
                    theme: 'modern',
                })
            }
        })
    })

    function refreshCart(){
        console.log('in current cart')
        var cartTable = $('.cart-table')
        var cartBody = cartTable.find('.cart-body')
        var productRows = cartBody.find('.cart-product')
        var currentUrl = window.location.href

        var refreshCartUrl = 'api/cart/';
        var refreshCartMethod = 'GET';
        var data = {};
        $.ajax({
            url: refreshCartUrl,
            method: refreshCartMethod,
            data: data,
            success: function (data){

                var hiddenCartRemoveForm = $('.cart-item-remove-form')
                if(data.products.length > 0){
                    productRows.html('')
                    i = data.products.length
                    $.each(data.products, function (index, value){
                        var newCartItemRemove = hiddenCartRemoveForm.clone()
                        newCartItemRemove.css('display', 'block')
                        newCartItemRemove.find('.cart-product-id').val(value.id)
                        cartBody.prepend(
                            '<tr>' +
                            '<th scope=\"row\">' + i + "</th>" +
                            "<td><a href='" + value.url + "'>" + value.title + '</a>' + newCartItemRemove.html() + '</td>' +
                            '<td>' + value.price + '</td>' +
                            '</tr>'
                        )
                        i--
                    })
                    cartBody.find('.cart-subtotal').text(data.subtotal)
                } else{
                    window.location.href = currentUrl;
                }
            },
            error: function (errorData){
                $.alert({
                    title: 'Opps!',
                    content: 'An Error occurred',
                    theme: 'modern',
                })
            }

        })
    }
})