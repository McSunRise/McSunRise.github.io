from django.shortcuts import HttpResponse, render
from django.views import View

def home(request):
    return render(request, "home.html")

class words_list(View):
    def get(self, request):
        words1, words2 = self.read_from_file()
        dictionary = dict(zip(words1, words2))
        print(dictionary)
        return render(request, "words.html", {'dictionary' : dictionary})

    def read_from_file(self):
        try:
            file = open("words.txt", "r", encoding="utf-8").read().splitlines()
        except FileNotFoundError:
            file = open("words.txt", "x", encoding="utf-8")
            return [], []
        words1 = []
        words2 = []
        for line in file:
            word1, word2 = line.split("-")
            words1.append(word1)
            words2.append(word2)
        return words1, words2

class add_word(View):
    def get(self, request):
        return render(request, "add_word.html")

    def post(self, request):
        data = request.POST
        word1 = data['word1']
        word2 = data['word2']
        with open("words.txt", "a", encoding="UTF-8") as file:
            file.write(word1 + '-' + word2 + '\n')
        return render(request, "add_word.html")

# Create your views here.
