document.getElementById('translator-form').addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent the default form submission
            submitForm();
        });

        function submitForm() {
            var fromLanguage = document.getElementById('fromLanguage').value;
            var toLanguage = document.getElementById('toLanguage').value;
            var textToTranslate = document.getElementById('textToTranslate').value;

            var xhr = new XMLHttpRequest();
            xhr.onreadystatechange = function () {
                if (xhr.readyState == 4) {
                    if (xhr.status == 200) {
                        var response = JSON.parse(xhr.responseText);
                        var translatedText = response.translated_text;
                        var pronunciation = response.pronunciation;

                        document.getElementById('translatedText').value = translatedText;
                        document.getElementById('pronunciation').value = pronunciation;
                    } else {
                        // Handle errors
                        console.error('Request failed with status:', xhr.status);
                    }
                }
            };

            xhr.open("POST", "/translate", true);
            xhr.setRequestHeader("Content-Type", "application/json");

            var data = JSON.stringify({
                "from_language": fromLanguage,
                "to_language": toLanguage,
                "text_to_translate": textToTranslate
            });

            xhr.send(data);
        }