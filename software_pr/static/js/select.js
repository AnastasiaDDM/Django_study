// // Select
// $('.slct').click(function(){
	// /* Заносим выпадающий список в переменную */
	// var dropBlock = $(this).parent().find('.drop');

	// /* Делаем проверку: Если выпадающий блок скрыт то делаем его видимым*/
	// if( dropBlock.is(':hidden') ) {
		// dropBlock.slideDown();

		// /* Выделяем ссылку открывающую select */
		// $(this).addClass('active');

		// /* Работаем с событием клика по элементам выпадающего списка */
		// $('.drop').find('li').click(function(){

			// /* Заносим в переменную HTML код элемента
			// списка по которому кликнули */
			// var selectResult = $(this).find('a').data('znach');
			// var selectResultName = $(this).find('a').html();

			// /* Находим наш скрытый инпут и передаем в него
			// значение из переменной selectResult */
			// $(this).parent().parent().find('input').val(selectResult);

			// /* Передаем значение переменной selectResult в ссылку которая
			// открывает наш выпадающий список и удаляем активность */
			// $(this).parent().parent().find('.slct').removeClass('active').html(selectResultName);

			// /* Скрываем выпадающий блок */
			// dropBlock.slideUp();
		// });

	// /* Продолжаем проверку: Если выпадающий блок не скрыт то скрываем его */
	// } else {
		// $(this).removeClass('active');
		// dropBlock.slideUp();
	// }

	// /* Предотвращаем обычное поведение ссылки при клике */
	// return false;
// });




              let inputs = document.querySelectorAll('.input__file');
              Array.prototype.forEach.call(inputs, function (input) {
                let label = input.nextElementSibling,
                  labelVal = label.querySelector('.input__file-button-text').innerText;
           
                input.addEventListener('change', function (e) {
                  let countFiles = '';
                  if (this.files && this.files.length >= 1)
                    countFiles = this.files.length;
           
                  if (countFiles)
                    label.querySelector('.input__file-button-text').innerText = 'Выбрано файлов: ' + countFiles;
                  else
                    label.querySelector('.input__file-button-text').innerText = labelVal;
                });
              });