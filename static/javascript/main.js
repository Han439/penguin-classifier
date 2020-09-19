// loader window

$(window).on('load', function() {
	let content = $('.filter-container')
	let loader = $('.loading')
	loader.fadeOut(750, function() {
		
		content.fadeIn(500)
	})

})


// radio button validation
function isRadioValidated(name) {
	let inputs = document.querySelectorAll(`input[name=${name}]`);
	for (i of inputs) {
		if (i.checked)
			return true
	}

	return false
}

function radioAlert() {
	let alertBox = document.querySelector(".alert");
	let alert = document.querySelector(".alert-container")
	alertBox.classList.add("animate");

	let alertBtn = document.querySelector('.alert-btn');
	alertBtn.addEventListener('click', (e) => {
		alertBox.classList.remove("animate");
	})
}


let sliders = document.querySelectorAll('.slider');
let values = document.querySelectorAll('.value');
let result = document.getElementById('result');
let results = result.children;

result.addEventListener('click', function(e) {
	if (e.target.localName == 'img')
		result.classList.add('full');
	else result.classList.remove('full');
})

for (i = 0; i < sliders.length; i++) {
	sliders[i].oninput = function() {
		let val = ((Number(this.value) - Number(this.min)) / (Number(this.max)-Number(this.min))) * 100
		$(this).siblings(".value").width(JSON.stringify(val) + "%")
		$(this).siblings(".tooltip").html(this.value)
		$(this).siblings(".tooltip").css("left", JSON.stringify(val) + "%")
	}
}


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

form = document.getElementById('filter-form');

form.addEventListener('submit', function(e) {
	e.preventDefault()
	let url = '/api/dt-predict/';

	// construc json data to be sent
	data = {};
	const formData = new FormData(this);
	for (let input of formData) {
		if (['island', 'sex'].includes(input[0])) {
			data[input[0]] = input[1]
		}else{ data[input[0]] = Number(input[1])}
	};

	// console.log(JSON.stringify(data))
	// console.log($(this).serialize())

	if (isRadioValidated('island') && isRadioValidated('sex')) {

		$.ajax({
			type: "POST",
			url: url,
			headers: {
				//'Content-type': 'application/json',
				'X-CSRFToken': csrftoken,
				'Accept': 'application/json; indent=4',
			},
			data: $(this).serialize(), // default rest parser (form-urlencoded contentype)
			// data: JSON.stringify(data)  // json rest parser (app/json contentype)
			dataType: "json",

			beforeSend: function() {
				$('.loading').fadeIn()
			},

			complete: function() {
				$('.loading').fadeOut()
			},

			success: function(res) {
				for (i = 0; i < results.length; i++) {
					if (res.result == results[i].getAttribute('data-prediction'))
						results[i].classList.remove('hidden')
					else results[i].classList.add('hidden')
				}
			},

			//error: function() {}
	})

	}else{
		radioAlert();
	}

})