from django.shortcuts import render


def board(request):
    context = {
        'board': [
            ['.', '.', 'C'],
            ['R', '.', '.'],
            ['.', 'F', '.'],
        ]
    }
    return render(request, 'game/board.html', context)
