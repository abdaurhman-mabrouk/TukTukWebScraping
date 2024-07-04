import tkinter as tk
from tkinter import messagebox, simpledialog, Scrollbar, Text, VERTICAL
import requests
from bs4 import BeautifulSoup


class MovieScraperApp:
    def __init__(self, master):
        self.master = master
        self.master.attributes("-fullscreen", True)  # Start in full-screen mode
        self.master.configure(background="white")  # Set background color to white

        self.setup_widgets()

    def setup_widgets(self):
        self.label = tk.Label(
            self.master,
            text="Welcome to Movie Scraper App",
            font=("Helvetica", 24),
            fg="black",
            bg="white",
        )
        self.label.pack(expand=True, fill="both")

        self.textbox = Text(
            self.master,
            wrap="word",
            font=("Helvetica", 14),
            fg="black",
            bg="white",
            insertbackground="black",
        )
        self.textbox.pack(expand=True, fill="both", padx=20, pady=20)

        scrollbar = Scrollbar(self.textbox, orient=VERTICAL, command=self.textbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.textbox.config(yscrollcommand=scrollbar.set)

        self.animate()

        self.setup_menus()

    def setup_menus(self):
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.quit_app)

        scrape_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Scrape", menu=scrape_menu)
        scrape_menu.add_command(label="Scrape Movies", command=self.scrape_pages)

        search_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Search", menu=search_menu)
        search_menu.add_command(label="Search Movies", command=self.movie_search)

        back_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Back", menu=back_menu)
        back_menu.add_command(label="Clear Output", command=self.clear_output)
        back_menu.add_command(label="Back to Main Menu", command=self.back_to_main_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about_info)

    def animate(self):
        self.fade_in_out()

    def fade_in_out(self):
        self.label.configure(fg="white")
        self.label.after(2000, lambda: self.label.configure(fg="black"))
        self.master.after(4000, self.animate)

    def scrape_pages(self):
        pageNum = simpledialog.askstring("Select Page Number", "Enter Page Number:")
        moviesQuantity = simpledialog.askstring(
            "Select Movies Quantity", "Enter Movies Quantity (1 to 30):"
        )

        if not pageNum or not moviesQuantity:
            messagebox.showwarning("Input Error", "Please enter valid input.")
            return

        if pageNum == "*":
            messagebox.showinfo("Info", "Scraping all pages. This may take a while.")
            pageNum = 1
            sourcePage = requests.get(
                f"https://t40.tuktukcinema1.buzz/category/movies-1/%D8%A7%D9%81%D9%84%D8%A7%D9%85-%D8%A7%D8%AC%D9%86%D8%A8%D9%8A/",
                timeout=10,
            )
            pagesNum = int(
                BeautifulSoup(sourcePage.content, "html.parser")
                .find("ul", {"class": "page-numbers"})
                .find_all("li")[-2]
                .find("a")
                .text.strip()
            )
        else:
            pagesNum = 1

        mainPage = requests.get(
            f"https://t40.tuktukcinema1.buzz/category/movies-1/%D8%A7%D9%81%D9%84%D8%A7%D9%85-%D8%A7%D8%AC%D9%86%D8%A8%D9%8A/?page={pageNum}",
            timeout=10,
        )

        src = mainPage.content
        soup = BeautifulSoup(src, "lxml")
        movieData = []
        moviesList = soup.find("ul", {"class": "Blocks--List"})
        moviesGenre = (
            soup.find("div", {"class": "archiveTitle"}).find("h1").text.strip()
        )
        moviesDivs = moviesList.find_all("div", {"class": "Block--Item"})

        if (
            not moviesQuantity.isdigit()
            or int(moviesQuantity) < 1
            or int(moviesQuantity) > 30
        ):
            moviesNum = len(moviesDivs)
        else:
            moviesNum = int(moviesQuantity)

        for i in range(pagesNum):
            for j in range(moviesNum):
                moviePageLink = moviesDivs[j].find("a").get("href")
                moviePageRes = requests.get(moviePageLink, timeout=10)
                moviePageElements = moviePageRes.content
                soup = BeautifulSoup(moviePageElements, "lxml")

                movieDiv = soup.find("div", {"class": "MainSingle"})

                movieNum = j
                movieName = (
                    movieDiv.find("div", {"class": "MasterSingleMeta"})
                    .find("h1")
                    .find("a")
                    .text
                )

                movieImageLink = (
                    movieDiv.find("div", {"class": "left"})
                    .find("div", {"class": "image"})
                    .find("img")
                    .get("src")
                )

                movieStory = (
                    movieDiv.find("div", {"class": "MasterSingleMeta"})
                    .find("div", {"class": "story"})
                    .find("p")
                    .text
                )

                movieTime = (
                    movieDiv.find("div", {"class": "MasterSingleMeta"})
                    .find("div", {"class": "MediaQueryRight"})
                    .find("ul", {"class": "RightTaxContent"})
                    .find_all("li")[0]
                    .find("strong")
                    .text
                )

                movieDate = (
                    movieDiv.find("div", {"class": "MasterSingleMeta"})
                    .find("div", {"class": "MediaQueryRight"})
                    .find("ul", {"class": "RightTaxContent"})
                    .find_all("li")[1]
                    .find("a")
                    .text
                )

                movieQuality = (
                    movieDiv.find("div", {"class": "MasterSingleMeta"})
                    .find("div", {"class": "MediaQueryRight"})
                    .find("ul", {"class": "RightTaxContent"})
                    .find_all("li")[3]
                    .find("a")
                    .text
                )

                movieVideoLink = (
                    movieDiv.find("div", {"class": "MasterSingleMeta"})
                    .find("div", {"class": "MediaQueryLeft"})
                    .find("div", {"class": "right"})
                    .find("a")
                    .get("href")
                )

                # Displaying in GUI
                self.textbox.insert("end", f"Movie Name: {movieName}\n")
                self.textbox.insert("end", f"Movie Link: {moviePageLink}\n")
                self.textbox.insert("end", f"Movie Image Link: {movieImageLink}\n")
                self.textbox.insert("end", f"Movie Story: {movieStory}\n")
                self.textbox.insert("end", f"Movie Time: {movieTime}\n")
                self.textbox.insert("end", f"Movie Date: {movieDate}\n")
                self.textbox.insert("end", f"Movie Quality: {movieQuality}\n")
                self.textbox.insert("end", f"Movie Watching Link: {movieVideoLink}\n\n")
                self.textbox.update_idletasks()

            if pageNum == "*":
                pageNum += 1
            else:
                messagebox.showinfo("Info", f"Page {pageNum} scraping completed.")

    def movie_search(self):
        searchKeyword = simpledialog.askstring("Search Movies", "Enter search keyword:")

        if not searchKeyword:
            messagebox.showwarning("Input Error", "Please enter a valid keyword.")
            return

        searchUrl = f"https://t40.tuktukcinema1.buzz/?s={searchKeyword}"
        searchPageRes = requests.get(searchUrl, timeout=10)
        searchPageElements = BeautifulSoup(searchPageRes.content, "html.parser")

        searchPageResults = searchPageElements.find("ul", {"class": "Blocks--List"})
        resultsDivs = searchPageResults.find_all("div", {"class": "Block--Item"})

        resultsNum = len(resultsDivs)

        if resultsNum == 0:
            messagebox.showinfo("Info", "No results found.")
            return

        self.textbox.delete(1.0, "end")

        self.textbox.insert("end", f"Search Results for '{searchKeyword}':\n\n")
        for i, result in enumerate(resultsDivs, start=1):
            resultMovieName = result.find("a").get("title")
            resultMovieLink = result.find("a").get("href")

            self.textbox.insert("end", f"{i}. {resultMovieName}\n")
            self.textbox.insert("end", f"   Movie Link: {resultMovieLink}\n\n")
            self.textbox.update_idletasks()

    def clear_output(self):
        self.textbox.delete(1.0, "end")

    def back_to_main_menu(self):
        self.textbox.delete(1.0, "end")
        self.label.configure(text="Welcome to Movie Scraper App")

    def show_about_info(self):
        messagebox.showinfo(
            "About", "Movie Scraper App\nVersion 1.0\nDeveloped by Your Name"
        )

    def quit_app(self):
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = MovieScraperApp(root)
    root.mainloop()
