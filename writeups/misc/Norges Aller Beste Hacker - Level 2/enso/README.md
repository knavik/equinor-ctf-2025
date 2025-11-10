# Norges aller beste hacker - Level 2


    Welcome to our most "advanced" cybersecurity challenge!

    You're still answering the same wonderfully realistic questions about meatball key storage and paranormal threat modeling, but now we're really keeping you in suspense.

    Are you ready to prove your elite cybersecurity expertise through pure determination and systematic guessing?

This challenge is a continuation of Level 1 which I solved quite manually. When we enter the Level 2 page we see a similar form with 50 multiple choice questions. I select all the first options and submit.

```json
{
  "anonymous": false,
  "deliveryDate": "2025-11-09T16:03:50.978+0000",
  "formReceiptText": "<h1 style=\"font-size: 3em;\">Try again!</h1>",
  "quizFeedback": { "maxScore": 50, "score": 16 },
  "receiptHeadline": "The form has been delivered",
  "requestEmail": false,
  "status": "success"
}

```
This time it is harder. No indication as to what questions are correct. There is nothing of value in the cookies or session state so I guess we are expected to make some sort of brute force here.


The request content looks like this

    ------geckoformboundary48cb33735a55648b63dbef8538f07b
    Content-Disposition: form-data; name="refererUrlHolder"

    https://ens-99d1a511-norges-aller-beste-hacker.ept.gg/
    ------geckoformboundary48cb33735a55648b63dbef8538f07b
    Content-Disposition: form-data; name="answersAsMap[684567].answerOption"

    942389
    ------geckoformboundary48cb33735a55648b63dbef8538f07b
    Content-Disposition: form-data; name="answersAsMap[684568].answerOption"

    942393
    ------geckoformboundary48cb33735a55648b63dbef8538f07b
    Content-Disposition: form-data; name="answersAsMap[684569].answerOption"

So the approach is to make a short program that uses the session cookie from firefox and builds up a form with all the answers and then changes one at a time to try to figure out which alternatives that changes the resulting score positively.

I notice that the form data start at 942389 and increases by 4 and the answerAsMap, the form element name, starts at 684567 and increases by 1.

So the main loop ended up like this
```c#
    public static async Task PostForm()
    {
        var client = new HttpClient();
        client.DefaultRequestHeaders.Add("Cookie", "session=.eJw1jVs...");
        var answers = new int[50];
        //all answers at 0 yields 16 correct answers
        var maxCorrect = 16;

        for (var i = 0; i < 50; i++)
        {
            for (var option = 0; option < 4; option++)
            {
                answers[i] = option;
                var score = await GetNumberOfCorrectAnswers(answers, client);
            
                if (score > maxCorrect)
                {
                    maxCorrect = score;
                    break;
                }

                if (score >= maxCorrect) continue;
                //if the answer is lower than before, 0 was the correct answer index
                answers[i] = 0;
                break;
            }
            Console.WriteLine($"answer:{i} - {answers[i]}");
        }
    }
```
And the method to post the form:

```c#
    private static async Task<int> GetNumberOfCorrectAnswers(int[] answers, HttpClient client)
    {
        var content = new MultipartFormDataContent();

        //add all elements to the form
        for (var i = 0; i < 50; i++)
        {
            var answer = (answers[i] + 942389 + (4*i)).ToString();
            content.Add(new StringContent(answer), $"answersAsMap[{684567 + i}].answerOption");
        }

        var res = await client.PostAsync(
            "https://ens-99d1a511-norges-aller-beste-hacker.ept.gg/answer/deliver.json?formId=160348&quizResultAsJson=false&elapsedTime=73731&retries=0",
            content);
        if (!res.IsSuccessStatusCode) return 0;
        var result = await res.Content.ReadAsStringAsync();
        var resultObj = JsonSerializer.Deserialize<QuizResponse>(result, new JsonSerializerOptions()
        {
            PropertyNameCaseInsensitive = true
        });
        if (resultObj.QuizFeedback.Score == 50)
        {
            Console.WriteLine("success: "+resultObj.FormReceiptText);
        }
        return resultObj.QuizFeedback.Score;
    }
```
And the contract.
```c#
public class QuizFeedbackDto
{
    public int MaxScore { get; set; }
    public int Score { get; set; }
}
public class QuizResponse
{
    public bool Anonymous { get; set; }
    public string DeliveryDate { get; set; }
    public string FormReceiptText { get; set; }
    public QuizFeedbackDto QuizFeedback { get; set; }
    public string ReceiptHeadline { get; set; }
    public bool RequestEmail { get; set; }
    public string Status { get; set; }
}
```
The result yielded:

    ...
    answer:45 - 0
    answer:46 - 0
    answer:47 - 1
    answer:48 - 2
    success: <h1 style="font-size: 3em;">EPT{m4st3rm1nd_brut3f0rc3_p4t13nc3_r3w4rd3d!}</h1>
    answer:49 - 3

Flag: `EPT{m4st3rm1nd_brut3f0rc3_p4t13nc3_r3w4rd3d!}`

---
  <center> <a href="https://enso.no" target="_blank">Made with ❤️ by Ensō</a>  </center>