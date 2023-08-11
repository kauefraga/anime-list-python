# ✉ Anime List Python is now archived.

I **reimplemented it with *Golang***, check here: [anime-archive](https://github.com/kauefraga/anime-archive)

---

<div align="center">
  <h1><code>Anime List</code></h1>

  <p>
    <strong>📖 A list to save all my viewed animes 📖</strong>
  </p>

  <p>
    <img
      alt="GitHub top language"
      src="https://img.shields.io/github/languages/top/kauefraga/anime-list.svg"
    />
    <img
      alt="Repository size"
      src="https://img.shields.io/github/repo-size/kauefraga/anime-list.svg"
    />
    <a href="https://github.com/kauefraga/anime-list/commits/main">
      <img
        alt="GitHub last commit"
        src="https://img.shields.io/github/last-commit/kauefraga/anime-list.svg"
      />
    </a>
    <img
      alt="GitHub LICENSE"
      src="https://img.shields.io/github/license/kauefraga/anime-list.svg"
    />
  </p>
</div>

> I used to write the animes that i watch right in a plain text file however,
i decided to create this project using Python because of its facilities and
packages that i wanted to try, like: _rich_ (beautiful formatter), _peewee_
(little orm) and _click_ (cli composer toolkit).

### Features

- **Fancy UI**: A minimal UI that exposes everything you need.
- **Colorized Outputs**: Everything looks better with some colors.
- **Nice help**: If you need some help, just use the flag `--help`.
- **Commands**:
  - `list`: query and show today animes
    - `list --all`: show all available animes
  - `create`: create an anime with a given title/description and save it
  - `find`: search for an anime with a title and return it with a url
    - `find --all`: return a list of nice websites
  - `save`: save the whole database into a csv file
  - `status`: list the available and unavailable websites for watching anime


## ⬇️ How to install and use it

1. Clone the repository and enter in
2. Install the dependencies
3. Run one of the commands listed above (at features)

```bash
git clone https://github.com/kauefraga/anime-list.git
cd anime-list

pip install -r requirements.txt

python3 src/main.py COMMAND
```
You are welcome to open issues and pull requests!

## 🛠 Technologies

- 🐍 [Python](https://www.python.org) - A programming language that lets you work quickly
and integrate systems more effectively.
- 🕶 [Click](https://pypi.org/project/click) - Composable command line interface toolkit
- 🗃 [Peewee](https://pypi.org/project/peewee) - Peewee is a simple and small ORM.
- 🎨 [Rich](https://pypi.org/project/rich) - Rich is a Python library for rich text and beautiful formatting in the terminal.
- 🛡 [Validators](https://pypi.org/project/validators) - A library for validating URLs
- 💾 [Sqlite](https://www.sqlite.org/index.html) - A small, fast, self-contained... A SQL database engine

## 📝 License

This project is licensed under the MIT License - See the [LICENSE](https://github.com/kauefraga/anime-list/blob/main/LICENSE) for more information.

---

<div align="center" display="flex">
  <img alt="Built with love" src="https://forthebadge.com/images/badges/built-with-love.svg">
  <img alt="Powered by coffee" src="https://forthebadge.com/images/badges/powered-by-coffee.svg">
</div>
