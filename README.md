# Rust Fiends

[![Build Status](https://travis-ci.com/Prejudice182/prej-milestone-four.svg?branch=master)](https://travis-ci.com/Prejudice182/prej-milestone-four)

Milestone Project Four: Full Stack Frameworks with Django - Code Institute

This e-commerce site was designed as my submission for my final milestone project for Code Institute's diploma in software development. The purpose of the site is to allow users to purchase in-game items for Rust.

Rust is a survival game, that allows players to go against one another in an open world scenario. Players spawn on a beach with nothing but a rock and torch to start them on their journey. Using these tools, players must farm for resources in order to craft tools, build bases and fight against other players.

A live version can be found deployed on Heroku [here.](https://rustfiends.herokuapp.com)

## UX

When I was planning my design for this project, I wanted to make it as simple as possible, but also replicate other e-commerce sites, as people now expect a certain layout on these sites.

- As a user, I want to be able to know which items are currently featured for sale.
- As a user, I want to see items sorted by price, so I can spend frugally (or not).
- As a user, I would like to be able to keep up to date with the latest goings on in the game.
- As an player with numerous hours, I want to get any advantage I can get, at any cost.
- As a new player, I want to know which items I should work my way up to.

## Design Choices

### Fonts

I chose to go with 2 fonts for the majority of text on the site:

- Bebas Neue - I chose this as it stands out nicely in headlines, has a clean style, and a suitable weight.

- Open Sans - This font is a easy to read san serif font, perfect for large blocks of text as it has a friendly appearance.

### Icons

- The shopping cart icon was used as users are expecting to see this in the navbar.
- Important facts are displayed on the home page using an icon suitable for purpose.
- Icons were used to display the logos in the footer, with Font Awesome layering used to fill in the background appropriately.

### Colours

- Rust: #ce422b

- The brand colour for this project was chosen as it matches the colour used in the Rust logo. This stands out nicely against the background of the site, and is used on secondary headings, buttons and forms throughout the site.

## Wireframes

I mocked up some wireframes for a desktop-first layout using Balsamiq

- [Home Page](/wireframes/home.png)
- [Products Page](/wireframes/products.png)
- [Cart Page](/wireframes/cart.png)
- [Checkout Page](/wireframes/checkout.png)

## Features

### Existing Features

#### Navbar

- Features on all pages
- Contains the Rust Fiends logo
- Dropdown menu containing the available categories
- Link to news articles pertaining to Rust
- Logged in users will see the cart icon and a logout link
- Others will see the sign up or log in links
- An admin user will see a link to the admin panel for ease of access

#### Footer

- Features on all pages
- Contains copyright info for Rust Fiends
- Links to Facebook, Twitch and Steam for Rust

#### Home Page

- Jumbotron containing attention grabbing image
- Introduction section with important facts laid out
- Featured categories for quick access to important items

#### Products Page

- Jumbotron containing an image of a shopfront from Rust
- Sort results by a variety of options
- Products displayed as images with their title and price underneath
- Each product links to their own details page, with more information
- Paginated to 6 products per page

#### Product Details Page

- Larger size view of the product image
- Name, price and description easily accessible
- Dropdown menu to select quantity to add to cart

#### Register Page

- Form for registering containing username, email and password fields
- Hints to help users understand what is needed in each field
- Redirect logged in users back to home page

#### Login Page

- Standard form for logging in, containing username and password fields
- Validates and returns any error found in form

#### Cart Page

- Contains a table listing all items in a users cart
- Each listing contains a thumbnail image of the product
- A minus and plus symbol to allow users to change quantities
- A cross is displayed to remove item from cart
- Total price is displayed at the foot of the table

#### Checkout Pages

- Form for user to input their billing address
- Fields are simple CharFields, no plugins were used to obtain list of countries or states
- If the user has ordered before, allow them to use saved address
- Verification that details are correct before proceeding to Stripe
- Stripe offers a hosted checkout page which I opted to use for payment details
- If user cancels from Stripe, return to cart page
- When user completes purchase, Stripe redirects back, sees confirmation

### Features Left to Implement

#### Emails

- On user register, or password change, send an email asking user to confirm these actions

#### Staff Page

- Allow staff to mark an order as shipped once payment has cleared

#### User Profiles

- Better customization of the default user model offered by Django

## Database

### Database Choice

- Django uses an ORM layer for working with SQL databases. Locally, an sqlite3 database was used during development
- On deployment, Heroku doesn't support sqlite3 so a PostgreSQL database was provisioned

### Models

#### User

The user model extends the AbstractUser model provided by Django, to allow for customization in the future.

#### Products App

##### Product

| Field        |          Validation           |              Field Type |
| ------------ | :---------------------------: | ----------------------: |
| Slug         |        editable=False         |               SlugField |
| Name         |        max-length=300         |               CharField |
| Main Image   |          blank=True           |              ImageField |
| Category     |   on_delete=models.CASCADE    | Foreign Key to Category |
| Preview Text |        max_length=200         |               TextField |
| Detail Text  |        max_length=1000        |               TextField |
| Price        | max_digits=5,decimal_places=2 |            DecimalField |

##### Category

| Field    |   Validation   |   Field Type |
| -------- | :------------: | -----------: |
| Slug     |                |    SlugField |
| Title    | max_length=300 |    CharField |
| Featured | default=False  | BooleanField |

#### Cart App

##### Cart

| Field    |        Validation        |          Field Type |
| -------- | :----------------------: | ------------------: |
| Customer | on_delete=models.CASCADE | Foreign Key to User |
| Created  |    auto_now_add=True     |       DateTimeField |
| Updated  |      auto_now=True       |       DateTimeField |
| Ordered  |      default=False       |        BooleanField |

- Cart also returns a total value of all items in a cart

##### CartItem

| Field    |        Validation        |                Field Type |
| -------- | :----------------------: | ------------------------: |
| Cart     | on_delete=models.CASCADE |       Foreign Key to Cart |
| Product  | on_delete=models.CASCADE |    Foreign Key to Product |
| Updated  |      auto_now=True       |             DateTimeField |
| Quantity |        default=1         | PositiveSmallIntegerField |

- CartItem returns a total value of quantity by price

#### Checkout App

##### BillingAddress

| Field            |        Validation         |          Field Type |
| ---------------- | :-----------------------: | ------------------: |
| User             | on_delete=models.CASCADE  | Foreign Key to User |
| Street Address 1 |      max_length=200       |           CharField |
| Street Address 2 | max_length=200,blank=True |           CharField |
| Town or City     |       max_length=50       |           CharField |
| County or State  | max_length=50,blank=True  |           CharField |
| Country          |       max_length=50       |           CharField |
| Postcode         | max_length=50,blank=True  |           CharField |

##### Order

| Field      |             Validation              |          Field Type |
| ---------- | :---------------------------------: | ------------------: |
| User       |      on_delete=models.CASCADE       | Foreign Key to User |
| Created    |          auto_now_add=True          |       DateTimeField |
| Total      |   max_digits=10,decimal_places=2    |        DecimalField |
| Payment ID | max_length=200,blank=True,null=True |           CharField |
| Order ID   | max_length=200,blank=True,null=True |           CharField |

##### OrderItem

This model is essentially a copy of CartItem, with the Cart foreign key switched to an Order foreign key

#### News App

##### Article

| Field        |        Validation        |          Field Type |
| ------------ | :----------------------: | ------------------: |
| Author       | on_delete=models.CASCADE | Foreign Key to User |
| Headline     |      max_length=100      |           CharField |
| Tag Line     |      max_length=100      |           CharField |
| Content      |                          |           TextField |
| Banner Image |        blank=True        |          ImageField |
| Created      |    auto_now_add=True     |       DateTimeField |
| Updated      |      auto_now=True       |       DateTimeField |

## Technologies Used

### Tools

- [Visual Studio Code](https://code.visualstudio.com/)
  - IDE used to develop this project
- [Django](https://www.djangoproject.com/)
  - Python framework used as backbone of project
- [Stripe](https://stripe.com/ie)
  - Payment platform used to handle and process card payments securely
- [Travis](https://travis-ci.com/)
  - Continuous Integration
- [Git](https://git-scm.com/)
  - Version Control, used to store each developmental change
- [Amazon AWS](https://aws.amazon.com)
  - Cloud Storage used to host images and static files
- [Heroku](https://www.heroku.com/)
  - Platform as a Service, used to host our deployed project
- [Bootstrap](https://getbootstrap.com/)
  - CSS Framework used to help style project
- [Font Awesome](https://fontawesome.com/)
  - Icon Library used when icons were needed
- [jQuery](https://jquery.com/)
  - Javascript Library, used for DOM manipulation
- [Am I Responsive](http://ami.responsivedesign.is/)
  - Website used to test responsiveness across different devices

## Testing

## Deployment

### Local

You must have the following tools installed to deploy this project locally:

- [Python](https://www.python.org/)
- Git

You must also have an account set up for the following services:

- Amazon AWS + S3 Bucket
- Stripe

1. Clone this repository

```
git clone https://github.com/Prejudice182/prej-milestone-four.git
```

2. Open a terminal or command prompt
3. Create a virtual environment, to keep the required libraries local to your project

```
# Windows
python -m venv env

# MacOS/Linux
sudo apt-get install python3-venv
python3 -m venv env
```

4. Activate your virtual environment

```
# Windows
env\Scripts\activate

# MacOS/Linux
source env/bin/activate
```

5. Install requirements

```
pip -r requirements.txt
```

6. Set up environment variables

```
# env.py

import os

os.environ.setdefault('SECRET_KEY', <key here>)
os.environ.setdefault('DEBUG', <True/False>)
os.environ.setdefault('STRIPE_PUBLISHABLE', <key here>)
os.environ.setdefault('STRIPE_SECRET', <key here>)
os.environ.setdefault('STRIPE_SUCCESS_URL', <URL here>)
os.environ.setdefault('STRIPE_CANCEL_URL', <URL here>)
os.environ.setdefault('AWS_ACCESS_KEY_ID', <key here>)
os.environ.setdefault('AWS_SECRET_ACCESS_KEY', <key here>)
```
7. Add this file to your .gitignore

```
# .gitignore

env.py
```

8. Migrate the models to create the database tables

```
python manage.py migrate
```

9. Create a superuser account so you can access the Django Admin Panel
```
python manage.py createsuperuser
```

10. Run the server locally
```
python manage.py runserver
```

11. You should now be able to navigate to the local link in the terminal. Append '/admin' to the end to access the admin panel, and log in using the user you just created

12. Create instances for Products, Categories and Articles

### Heroku

To deploy the project to Heroku, complete the following:

1. Create a new requirements.txt
```
pip freeze > requirements.txt
```

2. Create a Procfile
```
echo gunicorn rustfiends.wsgi:application > Procfile
```

3. Commit and push any changes to your Github repo:
```
git add .
git commit -m "Message goes here"
git push origin master
```

4. Create an app in your Heroku dashboard. Choose a snappy name, and choose the region where you would like your app located

5. In your apps dashboard, click the "Deploy" tab, look for "Deployment Method" section and choose Github

6. Select your repository that you have just pushed to

7. Click the "Settings" tab, and look for "Config Vars" section and click the "Reveal Config Vars" section

8. Set up your config vars with the same info you used for your local environment variables

9. Click the "Resources" tab, look for "Add-ons" section and add a Heroku Postgres - Hobby Dev database to your app 

10. Migrate your datbase models, and create a superuser by running these commands from your local machine:
```
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

11. Click the "Deploy" tab, go down to the "Manual Deploy" section, select the master branch of your repo, and "Deploy Branch"

## Credits

### Content

- All item names and images are property of Facepunch, from their game, Rust
- All other content was written by myself

### Media

- Images were retrieved from my local installation of the game, and uploaded to Amazon S3

### Acknowledgements

- I received inspiration for this site from visiting various e-commerce sites
- Thanks to my mentor, [Oluwaseun Owonikoko](https://github.com/seunkoko)
- Thanks to all members of the Code Institute Slack workspace
