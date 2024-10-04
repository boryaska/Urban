import time
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __repr__(self):
        return f"{self.nickname}"

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __repr__(self):
        return f"{self.title}"

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname:
                if user.password == hash(password):
                    self.current_user = user
                    # print('Вы авторизованы')
                    return
        # print('Ошибка авторизации')

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                # print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, hash(password), age)
        self.users.append(new_user)
        self.current_user = new_user
        # print('Вы зарегистрированы и авторизованы')

    def log_out(self):
        self.current_user = None

    def add(self, *vids):
        for vid in vids:
            duplicate = False
            for video in self.videos:
                if video.title == vid.title:
                    duplicate = True
                    break
            if not duplicate:
                self.videos.append(vid)

    def get_videos(self, search):
        search_answer = []
        for video in self.videos:
            if video.title.lower().find(search.lower()) != -1:
                search_answer.append(video.title)
        return search_answer

    def watch_video(self, film_title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == film_title:
                if video.adult_mode == True and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                for second in range(video.time_now, video.duration + 1):
                    print(second, end=' ', flush=True)
                    time.sleep(1)
                    video.time_now = second
                print("Конец видео")
                video.time_now = 0

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')