from PySide6 import QtWidgets, QtCore


from movie import get_movies, Movie

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self._setup_ui()
        self.populate_movies()
        self.setup_connections()
    


    def _setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self) # type: ignore
        self.setWindowTitle("CINE CLUB")
        self.title_field = QtWidgets.QLineEdit()
        self.add_btn = QtWidgets.QPushButton("Add")
        self.list_movie_field = QtWidgets.QListWidget()
        self.list_movie_field.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection) # type: ignore
        self.rmv_btn = QtWidgets.QPushButton("Remove movie(s)")

        self.layout.addWidget(self.title_field)
        self.layout.addWidget(self.add_btn)
        self.layout.addWidget(self.list_movie_field)
        self.layout.addWidget(self.rmv_btn)

    def setup_connections(self):
        self.title_field.returnPressed.connect(self.add_movie)
        self.add_btn.clicked.connect(self.add_movie)
        self.rmv_btn.clicked.connect(self.remove_movie)

    def populate_movies(self):
        movies = get_movies()

        for movie in movies:
            mv_title = QtWidgets.QListWidgetItem(movie.title)
            mv_title.setData(QtCore.Qt.UserRole, movie) # type: ignore
            self.list_movie_field.addItem(mv_title)


    def add_movie(self):
        title_mv = self.title_field.text()

        if not title_mv:
            return False
        
        movie_instance = Movie(title_mv)
        
        if movie_instance.add_to_movies():
            self.list_movie_field.clear()
            self.populate_movies()
    
        self.title_field.clear()

    def remove_movie(self):
        for selected_movies in self.list_movie_field.selectedItems():
            movie = selected_movies.data(QtCore.Qt.UserRole) #type: ignore
            movie.remove_from_movies()
            self.list_movie_field.takeItem(self.list_movie_field.row(selected_movies))




        # for movie in selected_movies:
        #     mv_instance = Movie(movie.text())
        #     mv_instance.remove_from_movies()
        
        # self.list_movie_field.clear()
        # self.populate_movies()




if __name__ == "__main__":
    app = QtWidgets.QApplication()
    win = App()
    win.show()
    app.exec_()
