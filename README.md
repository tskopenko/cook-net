
# COOK-NET

Welcome to the COOK-NET application! This Django-based project is designed to improve the connection between cooks by providing a platform for sharing recipes, tips, and culinary experiences. The application has been deployed and is accessible at [https://cook-net.onrender.com/](https://cook-net.onrender.com/).


## Features

- **Recipe Sharing:** Users can share their favorite recipes with the community.
- **Cooking Tips:** Find and share cooking tips and tricks.
- **Community Interaction:** Engage with other cooks, ask questions, and exchange ideas.
- **User Profiles:** Customize your profile and showcase your cooking expertise.
- **Search Functionality:** Easily search for recipes and cooking-related content.

## Usage

1. **Sign Up or Log In:** If you're new to COOK-NET, create an account to get started. If you already have an account, simply log in.
2. **Explore Recipes:** Browse through a wide range of recipes shared by fellow cooks.
3. **Share Your Recipes:** Contribute to the community by sharing your own recipes.
4. **Engage with the Community:** Like, comment, and interact with other users' posts.
5. **Discover Cooking Tips:** Explore cooking tips and tricks to enhance your culinary skills.
6. **Customize Your Profile:** Personalize your profile to showcase your cooking journey.

## Testing User

You can log in with the following credentials for a testing user:

- **Username:** user
- **Password:** geQaLkmmnQMs

## Technologies Used

- Django
- HTML/CSS
- PostgreSQL (Database)
- Render (Deployment)

## Getting Started

To run this project locally, follow these steps:


Clone this repository to your local machine

```bash
git clone https://github.com/tskopenko/COOK-NET.git
```

Navigate to the project directory

```bash
cd COOK-NET
```

Create and activate a virtual environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate  # For Windows
```

Install the required dependencies
```bash
pip install -r requirements.txt
```


Set up your PostgreSQL database and update the database configurations in settings.py
Create a PostgreSQL database named 'cook_net' with your preferred settings

Apply database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

Start the Django development server
```bash
python manage.py runserver
```
Access the application through your browser at http://localhost:8000

## Deployment

The COOK-NET application is deployed using Render and can be accessed at [https://cook-net.onrender.com/](https://cook-net.onrender.com/).

## Contributors

- Tymofii Skopenko (@tskopenko)

## Feedback and Support

If you encounter any issues or have feedback regarding the COOK-NET application, please contact us at [support@cooknet.com](mailto:support@cooknet.com).

We hope you enjoy using COOK-NET to enhance your cooking experience and connect with fellow cooks! Happy cooking! 🍳👩‍🍳👨‍🍳
