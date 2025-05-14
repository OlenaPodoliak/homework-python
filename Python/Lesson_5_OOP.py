from datetime import datetime, timedelta

# Base class for all feed records
class FeedRecord():
    def __init__(self, name):
        self.name = name

    def format(self):
        return f"{self.name.center(30, '-')}"


# News item
class News(FeedRecord):
    def __init__(self, text, city):
        self.name = "News"
        FeedRecord.__init__(self, self.name)
        self.text = text
        self.city = city

    def format(self):
        super().format()  # Сначала вызываем родительский метод
        date = datetime.now().strftime("%Y-%m-%d %H:%M")
        return f"{super().format()}\n{self.text}\n{self.city}, {date}\n\n"

# Advertising
class PrivateAd(FeedRecord):
    def __init__(self, text, expiration_date):
        self.name = "Private Ad"
        self.text = text
        self.expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")

    def format(self):
        days_left = (self.expiration_date - datetime.now()).days
        return f"{super().format()}\n{self.text}\nExpires in {days_left} day(s)\n\n"

# Job Posting
class JobPosting(FeedRecord):
    def __init__(self, position, company, salary):
        self.name = "Job Posting"
        self.position = position
        self.company = company
        self.salary = salary

    def format(self):
        post_id = f"{self.company[:3].upper()}-{datetime.now().strftime('%d%m%y%H%M')}"
        return f"{super().format()}\nPosition: {self.position}\nCompany: {self.company}\nSalary: {self.salary}\nRef ID: {post_id}\n\n"

# Tool to handle user input and publishing
class NewsFeedTool:
    def __init__(self, filename="news_feed.txt"):
        self.filename = filename

    def publish(self, record):
        with open(self.filename, 'a') as file:
            file.write(record.format())

    def run(self):
        print("Select record type to add:")
        print("1 - News")
        print("2 - Private Ad")
        print("3 - Job Posting")
        choice = input("Your choice: ")

        if choice == '1':
            text = input("Enter news text: ")
            city = input("Enter city: ")
            record = News(text, city)
        elif choice == '2':
            text = input("Enter ad text: ")
            date = input("Enter expiration date (YYYY-MM-DD): ")
            record = PrivateAd(text, date)
        elif choice == '3':
            position = input("Enter job position: ")
            company = input("Enter company name: ")
            salary = input("Enter salary: ")
            record = JobPosting(position, company, salary)
        else:
            print("Invalid selection. Choose from 1 to 3.")
            return

        self.publish(record)
        print(f"Record published to {self.filename}\n")

# Example usage
tool = NewsFeedTool()
tool.run()
