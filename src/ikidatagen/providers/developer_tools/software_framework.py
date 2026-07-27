from ..base_provider import BaseProvider


class SoftwareFrameworkProvider(BaseProvider):

    FRAMEWORKS = [
        # Frontend
        "React",
        "Next.js",
        "Vue.js",
        "Nuxt.js",
        "Angular",
        "Svelte",
        "SvelteKit",
        "SolidJS",
        "Qwik",
        "Astro",

        # Backend
        "Laravel",
        "Django",
        "Flask",
        "FastAPI",
        "Express.js",
        "NestJS",
        "Spring Boot",
        "ASP.NET Core",
        "Ruby on Rails",
        "Phoenix",

        # Full Stack
        "Meteor",
        "Blazor",
        "Remix",
        "T3 Stack",
        "AdonisJS",

        # Mobile
        "Flutter",
        "React Native",
        "Ionic",
        "Xamarin",
        ".NET MAUI",

        # Desktop
        "Electron",
        "Tauri",
        "Qt",
        "WPF",
        "Avalonia",

        # Data Engineering / Big Data
        "Apache Spark",
        "Apache Flink",
        "Apache Beam",
        "Kafka Streams",
        "Hadoop",

        # Machine Learning / AI
        "TensorFlow",
        "PyTorch",
        "Keras",
        "LangChain",
        "Haystack",

        # API / Microservices
        "Micronaut",
        "Quarkus",
        "Dropwizard",
        "Helidon",
        "gRPC"
    ]

    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        return self.get_random_data_by_list(self.FRAMEWORKS)
