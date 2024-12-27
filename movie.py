import os, json, logging

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "DATA", "movies.json")

def get_movies():
    with open(DATA_FILE, "r") as f:
        movies = [Movie(movie) for movie in json.load(f)]
    return movies

class Movie:
    def __init__(self, title: str) -> None:
        self.title = title.title()

    def __str__(self) -> str:
        return f"{self.title}"
    
    def _get_movies(self):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def _write_movies(self, movies):
        with open(DATA_FILE, "w") as f:
            json.dump(movies, f, indent=4)

    def add_to_movies(self):
        movies = self._get_movies()

        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"Movie {self.title} already added...")
            return False
        
    def remove_from_movies(self):
        movies = self._get_movies()

        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            logging.info(f"{self.title} removed from movies...")
            return True
        else:
            logging.warning(f"{self.title} not in movies...")
            return False

if __name__ == "__main__":
    m = get_movies()
    print(m)