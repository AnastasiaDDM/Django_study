  

// Ф-ия для стилизации селекта (выпадающего списка) 
function select_style() {

  $('.slct').click(function(){
		/* Заносим выпадающий список в переменную */
		var dropBlock = $(this).parent().find('.drop');

		/* Делаем проверку: Если выпадающий блок скрыт то делаем его видимым*/
		if( dropBlock.is(':hidden') ) {
			dropBlock.slideDown();

			/* Выделяем ссылку открывающую select */
			$(this).addClass('active');

			/* Работаем с событием клика по элементам выпадающего списка */
			$(dropBlock).find('li').click(function(){

				/* Заносим в переменную HTML код элемента
				списка по которому кликнули */
				var selectResult = $(this).find('a').data('value');
				var selectResultName = $(this).find('a').html();

				/* Находим наш скрытый инпут и передаем в него
				значение из переменной selectResult */
				$(this).parent().parent().find('input').val(selectResult).trigger('change');

				/* Передаем значение переменной selectResult в ссылку которая
				открывает наш выпадающий список и удаляем активность */
				$(this).parent().parent().find('.slct').removeClass('active').html(selectResultName);

				/* Скрываем выпадающий блок */
				dropBlock.slideUp();
			});

		/* Продолжаем проверку: Если выпадающий блок не скрыт то скрываем его */
		} 
		else {
			$(this).removeClass('active');
			dropBlock.slideUp();
		}

		/* Предотвращаем обычное поведение ссылки при клике */
		return false;
    });
    
    $('.slct').each(function(){
        if ($(this).parent().find('input').val().length > 0)
        {
            selectBox = this;
            find = $(this).parent().find('input').val();
            $(this).parent().find('.drop li a').each(function()
            {
                if ($(this).data('value') == find)
                {
                    $(selectBox).html($(this).html());
                }
            })
        }
    });
}



// Ф-ия сворачивания и разворота поиска
function search_roll() {

	if ($( window ).width() < 600) {
			$( ".search_roll_up" ).hide();
			$( ".search_div_fieldset" ).slideUp( "slow", function() {
			$( ".search_roll_down" ).show();
		});
		
	}
	else {
		$( ".search_roll_down" ).hide();
		$( ".search_div_fieldset" ).slideDown( "slow", function() {
			$( ".search_roll_up" ).show();
		});
	}
		  
    $( ".search_roll_up" ).click(function() {
      $( this ).hide();

      $( ".search_div_fieldset" ).slideUp( "slow", function() {
		$( ".search_roll_down" ).show();
      });
    });

    $( ".search_roll_down" ).click(function() {
      $( this ).hide();

      $( ".search_div_fieldset" ).slideDown( "slow", function() {
		$( ".search_roll_up" ).show();
      });
	});
}


// Ф-ия корректировки работы input и textarea (для label)
function input_filled(type)
{
  $('.'+type+'_style '+type).each(function(){

		// Это вызов ф-ии для того, как страница загрузилась и еще не менялась 
		var element = this;
		input_filled_addClass(type, element);

		// Это вызов ф-ии для отслеживания изменеения полей
		$(this).change(function(){
			var element = this;
			input_filled_addClass(type, element);
		});
  });
}

// Ф-ия корректировки работы input и textarea добавление класса
function input_filled_addClass(type, element)
{
      if ($(element).val().length > 0)
      {
        $(element).addClass(type+"_filled");
      }
      else
      {
        $(element).removeClass(type+"_filled");  
      }
}


// Ф-ия раскрытия списка всех возможных областей (поиск в каталоге)
function areas_more() {
	$( ".areas_more" ).click(function() {

	  if ($( ".all_areas" ).attr('style') == 'display: none;' ) {
		$( ".areas_more" ).html( "свернуть" );
	  }
	  else {
		$( ".areas_more" ).html( "еще..." );
	  }
	  
	  $( ".all_areas" ).slideToggle( 300, function() {
	  });

	});
}
 


function read_more_text_roll() {
	$( ".text_roll" ).click(function() {
		var target_id= $(this).data("target");
        if ($("#"+target_id).attr('style') == 'display: none;' ) {
          $( ".text_roll" ).html( "Свернуть" );
        }
        else {
          $( ".text_roll" ).html( "Читать полностью" );
        }
        
        $("#"+target_id).slideToggle( "slow", function() {
        });
      });
}



// Ф-ия прорисовки формы ответа в обсуждениях и показ комментариев
function comments_form_answer() {

    // Удаляем обработчики событий определенных ранее
    $( ".btn_answer" ).off();
    $( ".btn_answer_two" ).off();

    $( ".btn_answer" ).click( function () {
	
		// Показ всех кнопок Ответить
        $(".btn_answer").show(500);
        
        // Скрытие текущей нажатой кнопки Отвтеить 
        $(this).hide(500);
        var elem = this;
        var target = $("[data-rel='single_form_answer']");
    
		if (target.length ) {
			// Скрытие всех форм ответа и уничтожение
			target.hide(500, function () {
				target.detach();
				comments_form_answer_show_1(elem)
			});
		}
		else
		{
			comments_form_answer_show_1(elem)
		}
    
    });
    
    $( ".btn_answer_two" ).click(function () {

        // Показ всех кнопок Ответить
        $(".btn_answer_two").show(500);

        // Скрытие текущей нажатой кнопки Отвтеить 
        $(this).hide(500);
		var elem = this;
		var target = $("[data-rel='single_form_answer']");

		if (target.length ) {
			// Скрытие всех форм ответа и уничтожение
			target.hide(500, function () {
				target.detach();
				comments_form_answer_show_2(elem)
			});
		}
		else
		{
			comments_form_answer_show_2(elem)
        }
        
        comment_roll();

    });

    
}

// Ф-ия разворота/сворачивания комментариев
function comment_roll()
{
    // Удаляем обработчики событий определенных ранее
    $( ".comment_roll" ).off();
    $( ".btn_rollup" ).off();

    // Нажатие кнопки просмотра комментариев 
    $( ".comment_roll" ).click(function() {

        var com_data = $(this).data("target");
        
        // Разворот/сворачивание комментариев
        $( "#"+com_data+" .discussion_comment" ).slideToggle( "slow" );
    });
    
    // Нажатие кнопки сворачивания комментариев 
    $( ".btn_rollup" ).click(function() {
    
        // Разворот/сворачивание комметнариев
        $( this ).parents(".discussion_comment").slideToggle( "slow" );
    });
}


function comments_form_answer_show_2(elem)
{
    // Копирование шаблона формы ответа
    var form = $( "#pattern_form_answer").html();

    // Вставка формы ответа
    $(elem).parents(".discussion").append( $(form) );

	// Добавление атрибута, по которому потом будет удаляться эта форма
    var single_form_answer = $( ".discussion" ).children( ".copy_form_answer" )
    single_form_answer.attr( "data-rel", "single_form_answer" );

	// Берем ID дискуссии в начале блока этой дискуссии в виде dis_1 и проставляем в скрытое поле
	var id = $(elem).parents(".discussion").attr('id').split('_')[1];  
    single_form_answer.find("form").attr( "data-comment", "form_comment" );
    single_form_answer.find("[name='id_discussion']").val(id);

    // Показ формы
    $("[data-rel='single_form_answer']").show(500);

	// Инициализация необохдимых ф-ий для новых объектов
    comments_form_answer_hide();
    input_filled('input');
    input_filled('textarea');
    append_comment(); // Для привязки события submit
}

function comments_form_answer_show_1(elem)
{
    // Копирование шаблона формы ответа
    var form = $( "#pattern_form_answer").html();

    // Вставка формы ответа
    $(elem).parent().append( $(form) );

    // Добавление атрибута, по которому потом будет удаляться эта форма
    var single_form_answer = $(elem).siblings(".copy_form_answer")
    single_form_answer.attr( "data-rel", "single_form_answer" );

    // Берем ID дискуссии в начале блока этой дискуссии в виде dis_1 и проставляем в скрытое поле
    var id = $(elem).parents(".discussion").attr('id').split('_')[1]; 
    single_form_answer.find("form").attr( "data-comment", "form_comment" );
    single_form_answer.find("[name='id_discussion']").val(id);

    // Показ формы
    $("[data-rel='single_form_answer']").show(500);

	// Инициализация необохдимых ф-ий для новых объектов
    comments_form_answer_hide();
    input_filled('input');
    input_filled('textarea');
    append_comment(); // Для привязки события submit
}

// Ф-ия сворачивания формы ответа и отображение кнопки ответа
function comments_form_answer_hide() 
{
	$(".btn_cancel").click(function() {
		comments_form_answer_hide_action($(this).parents(".copy_form_answer"))
	});
}

// Вспомогательная ф-ия для сворачивания форм
function comments_form_answer_hide_action(elem) 
{ 
		// Скрытие текущей формы ответа
		elem.hide(500 , function () {
			$(this).parents(".copy_form_answer").detach();
		});

		// Показ всех кнопок Ответить
		$(".btn_answer").show(500);
		$(".btn_answer_two").show(500);
}


// Ф-ия управления виджетами, каруселями ПО
function carousel_soft(target) {
	$('#'+target).slick({
		infinite: true,
		slidesToShow: 3,
		slidesToScroll: 1,
		speed: 300,
		autoplay: true,
		autoplaySpeed: 2000,
		respondTo: 'min',
		
		responsive: [
			{
			breakpoint: 1024,
			settings: {
				slidesToShow: 3,
				slidesToScroll: 1,
				infinite: true,
			}
			},
			{
			breakpoint: 790,
			settings: {
				slidesToShow: 2,
				slidesToScroll: 1
			}
			},
			{
			breakpoint: 480,
			settings: {
				slidesToShow: 1,
				slidesToScroll: 1
			}
			}
		],
		arrows:true,
		appendArrows: $("#"+target+"_container"),
		prevArrow:'<i class="fa fa-angle-left pos_center widget_arrows" aria-hidden="true" ></i>',
		nextArrow:'<i class="fa fa-angle-right pos_center widget_arrows" aria-hidden="true"></i>',
		
	})
}
  

// Ф-ия инициализации input для даты
function datepicker_init() {
	if ($( window ).width() < 600) {
		$('.search_datepicker').each(function() {
			$( this  ).attr( "type", "date" );
		});
		
	}
	else {
			$('.search_datepicker').datepicker({
				language: 'ru',
				autoClose: true,
				// minDate: new Date() // Now can select only dates, which goes after today
			});
	}
}


//Ф-ия для очистки формы поиска
function form_search_reset()
{
	$("[data-rel='form_search']").click( function () {

		// Получение формы поиска
        current_form = $(this).parents($("[data-target='form_search']"));
        current_form.find( "input" ).val('').attr("checked", false);
        input_filled('input');
        input_filled('textarea');
    });
}



//  jQuery(document).ready(function () {
	
// 	select_style();
// 	input_filled();
// 	textarea_filled();
// 	search_roll();
// 	areas_more();
// 	comments_form_answer();
// 	datepicker_init();
// })

function form_validate(f, rules, messages)
{
  f.validate({
  errorPlacement: function(error, element)
  {
    element.parent().after( error);
  },
   highlight: function(element, errorClass, validClass)
  {
    $(element).parent().removeClass("input_style_valid").addClass("input_style_invalid");
  },
  unhighlight: function(element, errorClass, validClass)
  {
    $(element).parent().next(".input_style_error").remove();
    $(element).parent().removeClass("input_style_invalid").addClass("input_style_valid");
  },
  errorClass: "pos_left_for_text input_style_error",
  validClass: "",
  errorElement: "div",
  rules: rules,
  messages: messages
  });  
  
  
}


// Ф-ия для избранного
function favourite()
{
	$("[data-target='favourite']").click( function () {

        // Получение формы поиска
        var id = $(this).data("id");
        var url = $(this).data("url");
        tag_i = $(this).find( "i" )

        $.get( url + id)
            .done(function( data ) {

                if (data.result == true) {
                    $(tag_i).removeClass("button_like").addClass("button_like_true");
                }
                else {
                    $(tag_i).removeClass("button_like_true").addClass("button_like");
                }
            })
            .fail(function() {
                // alert( "error" );
              })
              .always(function() {
                // alert( "finished" );
              });
    });
}


// Ф-ия для отправки формы обсуждения
function append_discussion()
{
	// Удаляем обработчики событий определенных ранее
    $( "#form_discussion" ).off();

    // Форма добавления обсуждения
    $( "#form_discussion" ).submit(function( event ) {

        event.preventDefault();

        var options = { 
            success:    function(data) { 
                // Вставка обсуждения
                if (!is_error(data)) // Проверка наличия ошибка в ответе с сервера
                {
                    $('#container_discussions').append(data.result);  // Ошибки нет, добавляем обсуждение
                    comments_form_answer();
                    append_comment();    
                    comment_roll();                                
                }

            } 
        }; 

        $('#form_discussion').ajaxSubmit(options);
        $('#form_discussion').resetForm();
        input_filled('input');
        input_filled('textarea');

    });

}


// Ф-ия для отправки формы комментария
function append_comment()
{
    	// Удаляем обработчики событий определенных ранее
        $( "[data-comment='form_comment']" ).off();

        // Форма добавления комментария
        $( "[data-comment='form_comment']" ).submit(function( event ) {

            event.preventDefault();
            var elem = this;
            var container_discussion = $( elem ).parents(".discussion");

            // Элемент, в конец которого будет добавлен блок ответа
            var container = $( container_discussion ).find("[data-comment=container_comment]");

            if (!container.length) // Нет ранее добавленных комментариев
            {
                // Элемент, в конец которого будет добавлен блок ответа
                // container = $( container_discussion ).find(".discussion_comment");
                // container = container_discussion;
                container = $( container_discussion ).find(".comment_roll");
                
            }

            var options = { 
        
                success:    function(data) { 
    
                    if (!is_error(data)) // Проверка наличия ошибка в ответе с сервера
                    {
                        container.append(data.result); // Ошибки нет, добавляем комментарий
                        $(elem).resetForm(); // Сбрасываем форму
    
                        comment_count_change(container_discussion);
                        input_filled('input');
                        input_filled('textarea')
                        comments_form_answer_hide_action($(elem)); // Закрываем форму
                        comments_form_answer();                    
                    }
                } 
            }; 

            // Отправка ajaxForm 
            $(this).ajaxSubmit(options);

        });
}


// Ф-ия приверки не пришел ли ошибочный ответ - если ошибка - выводим на экран
function is_error(data) 
{
    if (data.status == 'error')
    {
        alert(data.error_text); // Лучше потом сделать какое-то нормальное диалоговое окно
        return true
    }
    return false;
}


// Ф-ия увеличивающая количество комментариев 
function comment_count_change(container_discussion) 
{
    var comment_count_elem = $(container_discussion).find("[data-rel=comment_count]");
    var new_count = parseInt(comment_count_elem.html()) + 1;
    comment_count_elem.html(new_count)
}