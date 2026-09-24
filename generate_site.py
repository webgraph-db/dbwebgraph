import os

WORKSPACE = r"c:\Users\A C E R\OneDrive\Desktop\Db WebGraphsit"
os.makedirs(WORKSPACE, exist_ok=True)

HEADER = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Db WebGraph</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <!-- AOS Animation CSS -->
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <!-- Typed JS -->
    <script src="https://unpkg.com/typed.js@2.1.0/dist/typed.umd.js"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: { sans: ['Inter', 'sans-serif'] },
                    colors: {
                        primary: '#1e3a8a', // Deep Blue
                        secondary: '#f97316', // Orange
                        dark: '#0f172a', // Navy
                        light: '#f8fafc',
                    }
                }
            }
        }
    </script>
    <style>
        /* Custom Scrollbar */
        ::-webkit-scrollbar { width: 8px; }
        ::-webkit-scrollbar-track { background: #f1f5f9; }
        ::-webkit-scrollbar-thumb { background: #94a3b8; border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: #f97316; }

        /* Glass Navbar */
        .glass-nav { background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); border-bottom: 1px solid rgba(226, 232, 240, 0.6); }

        /* Fancy Hover Effects */
        .card-hover { transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); }
        .card-hover:hover { transform: translateY(-8px); box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.1); }
        
        .icon-bounce i { transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1); }
        .icon-bounce:hover i { transform: scale(1.15) translateY(-5px); }

        .btn-glow { transition: all 0.3s ease; }
        .btn-glow:hover { box-shadow: 0 0 20px rgba(249, 115, 22, 0.4); transform: translateY(-2px); }
        
        .text-gradient { background: linear-gradient(135deg, #f97316, #fb923c); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        
        /* SVG Wave Divider */
        .wave-divider { position: absolute; bottom: 0; left: 0; width: 100%; overflow: hidden; line-height: 0; transform: rotate(180deg); z-index: 10; }
        .wave-divider svg { display: block; width: calc(100% + 1.3px); height: 60px; }
        .wave-divider .shape-fill { fill: #f8fafc; }
        
        .timeline-dot::before { content: ''; position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%); width: 24px; height: 24px; border-radius: 50%; background: #f97316; border: 4px solid white; box-shadow: 0 0 10px rgba(0,0,0,0.1); z-index: 10; }
    </style>
</head>
<body class="bg-light text-slate-800 flex flex-col min-h-screen selection:bg-secondary selection:text-white">
    <!-- Navbar -->
    <nav id="navbar" class="fixed w-full top-0 z-50 glass-nav transition-all duration-300">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-20 items-center">
                <div class="flex-shrink-0 flex items-center">
                    <a href="index.html" class="text-2xl font-extrabold text-primary flex items-center gap-2 transform transition hover:scale-105">
                        <i class="fas fa-layer-group text-secondary drop-shadow-md"></i> Db WebGraph
                    </a>
                </div>
                <div class="hidden lg:flex space-x-4 xl:space-x-6 items-center text-sm xl:text-base font-semibold">
                    <a href="index.html" class="text-slate-600 hover:text-secondary transition relative group">Home<span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-secondary transition-all group-hover:w-full"></span></a>
                    <a href="about.html" class="text-slate-600 hover:text-secondary transition relative group">About<span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-secondary transition-all group-hover:w-full"></span></a>
                    <a href="web-development.html" class="text-slate-600 hover:text-secondary transition relative group">Web Dev<span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-secondary transition-all group-hover:w-full"></span></a>
                    <a href="graphic-design.html" class="text-slate-600 hover:text-secondary transition relative group">Graphic Design<span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-secondary transition-all group-hover:w-full"></span></a>
                    <a href="education.html" class="text-slate-600 hover:text-secondary transition relative group">Education<span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-secondary transition-all group-hover:w-full"></span></a>
                    <a href="training.html" class="text-slate-600 hover:text-secondary transition relative group">Training<span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-secondary transition-all group-hover:w-full"></span></a>
                    <a href="portfolio.html" class="text-slate-600 hover:text-secondary transition relative group">Portfolio<span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-secondary transition-all group-hover:w-full"></span></a>
                    <a href="blog.html" class="text-slate-600 hover:text-secondary transition relative group">Blog<span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-secondary transition-all group-hover:w-full"></span></a>
                    <a href="contact.html" class="text-slate-600 hover:text-secondary transition relative group">Contact<span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-secondary transition-all group-hover:w-full"></span></a>
                </div>
                <div class="hidden lg:flex items-center space-x-3">
                    <a href="contact.html" class="bg-primary text-white px-5 py-2.5 rounded-full hover:bg-blue-800 transition shadow-lg btn-glow font-bold">Start Your Project</a>
                </div>
                <button class="lg:hidden text-slate-600 text-2xl focus:outline-none" onclick="document.getElementById('mobile-menu').classList.toggle('hidden')">
                    <i class="fas fa-bars"></i>
                </button>
            </div>
        </div>
        <!-- Mobile Menu -->
        <div id="mobile-menu" class="hidden lg:hidden bg-white/95 backdrop-blur-md border-t border-slate-100 absolute w-full z-40 shadow-xl">
            <div class="px-6 py-6 flex flex-col space-y-4 text-slate-700 font-semibold text-lg">
                <a href="index.html" class="hover:text-secondary">Home</a>
                <a href="about.html" class="hover:text-secondary">About</a>
                <a href="web-development.html" class="hover:text-secondary">Web Development</a>
                <a href="graphic-design.html" class="hover:text-secondary">Graphic Design</a>
                <a href="education.html" class="hover:text-secondary">Education</a>
                <a href="training.html" class="hover:text-secondary">Training</a>
                <a href="portfolio.html" class="hover:text-secondary">Portfolio</a>
                <a href="blog.html" class="hover:text-secondary">Blog</a>
                <a href="contact.html" class="hover:text-secondary">Contact</a>
                <div class="pt-4 flex flex-col gap-3">
                    <a href="contact.html" class="bg-primary text-white px-4 py-3 rounded-lg text-center shadow">Start Your Project</a>
                </div>
            </div>
        </div>
    </nav>
    <main class="flex-grow pt-20">
"""

FOOTER = """
    </main>
    
    <!-- Back to Top Button -->
    <button id="backToTop" class="fixed bottom-8 right-8 bg-secondary text-white w-12 h-12 rounded-full shadow-xl flex items-center justify-center text-xl opacity-0 pointer-events-none translate-y-10 transition-all duration-300 z-50 hover:bg-orange-600 hover:-translate-y-2 hover:shadow-orange-500/50" onclick="window.scrollTo({top: 0, behavior: 'smooth'})">
        <i class="fas fa-arrow-up"></i>
    </button>

    <footer class="bg-dark text-white pt-20 pb-8 border-t-4 border-secondary mt-auto relative overflow-hidden">
        <div class="absolute top-0 right-0 w-64 h-64 bg-primary/20 rounded-full blur-[80px] -translate-y-1/2 translate-x-1/3"></div>
        <div class="absolute bottom-0 left-0 w-64 h-64 bg-secondary/10 rounded-full blur-[80px] translate-y-1/2 -translate-x-1/3"></div>
        
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-16">
                <div class="col-span-1 lg:col-span-2" data-aos="fade-up">
                    <h2 class="text-3xl font-extrabold flex items-center gap-2 mb-3"><i class="fas fa-layer-group text-secondary"></i> Db WebGraph</h2>
                    <p class="text-slate-300 text-lg mb-2">Your Digital Identity Partner</p>
                    <p class="text-secondary font-bold text-xl mb-6">सीप सिकौँ, आत्मनिर्भर बनौँ!</p>
                    <p class="text-sm text-slate-400 max-w-md leading-relaxed mb-6">
                        We don't just create digital products for you; we help you learn how to create and manage them yourself. A professional digital agency combined with a practical digital learning platform.
                    </p>
                    <div class="flex space-x-4">
                        <a href="#" class="w-10 h-10 rounded-full bg-slate-800 flex items-center justify-center hover:bg-secondary hover:text-white transition transform hover:-translate-y-1 shadow-lg"><i class="fab fa-facebook-f"></i></a>
                        <a href="#" class="w-10 h-10 rounded-full bg-slate-800 flex items-center justify-center hover:bg-secondary hover:text-white transition transform hover:-translate-y-1 shadow-lg"><i class="fab fa-youtube"></i></a>
                        <a href="#" class="w-10 h-10 rounded-full bg-slate-800 flex items-center justify-center hover:bg-secondary hover:text-white transition transform hover:-translate-y-1 shadow-lg"><i class="fab fa-tiktok"></i></a>
                        <a href="#" class="w-10 h-10 rounded-full bg-slate-800 flex items-center justify-center hover:bg-secondary hover:text-white transition transform hover:-translate-y-1 shadow-lg"><i class="fab fa-linkedin-in"></i></a>
                    </div>
                </div>
                <div data-aos="fade-up" data-aos-delay="100">
                    <h3 class="text-lg font-bold mb-6 border-b border-slate-700 pb-2 inline-block">Quick Links</h3>
                    <ul class="space-y-3 text-slate-400 text-sm font-medium">
                        <li><a href="index.html" class="hover:text-secondary transition flex items-center gap-2 group"><i class="fas fa-chevron-right text-xs text-slate-600 group-hover:text-secondary transition"></i> Home</a></li>
                        <li><a href="about.html" class="hover:text-secondary transition flex items-center gap-2 group"><i class="fas fa-chevron-right text-xs text-slate-600 group-hover:text-secondary transition"></i> About</a></li>
                        <li><a href="web-development.html" class="hover:text-secondary transition flex items-center gap-2 group"><i class="fas fa-chevron-right text-xs text-slate-600 group-hover:text-secondary transition"></i> Web Development</a></li>
                        <li><a href="graphic-design.html" class="hover:text-secondary transition flex items-center gap-2 group"><i class="fas fa-chevron-right text-xs text-slate-600 group-hover:text-secondary transition"></i> Graphic Design</a></li>
                        <li><a href="training.html" class="hover:text-secondary transition flex items-center gap-2 group"><i class="fas fa-chevron-right text-xs text-slate-600 group-hover:text-secondary transition"></i> Master Training</a></li>
                        <li><a href="portfolio.html" class="hover:text-secondary transition flex items-center gap-2 group"><i class="fas fa-chevron-right text-xs text-slate-600 group-hover:text-secondary transition"></i> Portfolio</a></li>
                    </ul>
                </div>
                <div data-aos="fade-up" data-aos-delay="200">
                    <h3 class="text-lg font-bold mb-6 border-b border-slate-700 pb-2 inline-block">Contact Us</h3>
                    <ul class="space-y-4 text-slate-400 text-sm font-medium">
                        <li class="flex items-start gap-3 hover:text-white transition cursor-pointer"><i class="fas fa-map-marker-alt mt-1 text-secondary"></i><span>Kathmandu, Nepal</span></li>
                        <li class="flex items-center gap-3 hover:text-white transition cursor-pointer"><i class="fas fa-phone text-secondary"></i><span>+977 9800000000</span></li>
                        <li class="flex items-center gap-3 hover:text-white transition cursor-pointer"><i class="fas fa-envelope text-secondary"></i><span>contact@dbwebgraph.com</span></li>
                        <li class="flex items-center gap-3 hover:text-white transition cursor-pointer"><i class="fab fa-whatsapp text-secondary text-lg"></i><span>WhatsApp Available</span></li>
                    </ul>
                </div>
            </div>
            <div class="border-t border-slate-800 pt-8 flex flex-col md:flex-row justify-between items-center text-sm text-slate-500">
                <p>&copy; 2026 Db WebGraph. All Rights Reserved.</p>
                <p class="mt-4 md:mt-0">Founded by <a href="about.html" class="text-secondary font-bold hover:underline">Dharbindra BK</a></p>
            </div>
        </div>
    </footer>

    <!-- AOS Script -->
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        AOS.init({ once: true, offset: 60, duration: 800, easing: 'ease-out-cubic' });

        window.addEventListener('scroll', () => {
            const btn = document.getElementById('backToTop');
            const nav = document.getElementById('navbar');
            if (window.scrollY > 300) {
                btn.classList.remove('opacity-0', 'pointer-events-none', 'translate-y-10');
                btn.classList.add('opacity-100', 'translate-y-0');
                nav.classList.add('shadow-md');
            } else {
                btn.classList.add('opacity-0', 'pointer-events-none', 'translate-y-10');
                btn.classList.remove('opacity-100', 'translate-y-0');
                nav.classList.remove('shadow-md');
            }
        });
        
        document.addEventListener('DOMContentLoaded', function() {
            if(document.getElementById('typed-text')) {
                new Typed('#typed-text', {
                    strings: ['Identity Partner', 'Creative Agency', 'Learning Platform'],
                    typeSpeed: 60,
                    backSpeed: 40,
                    backDelay: 2000,
                    loop: true
                });
            }
        });
    </script>
</body>
</html>
"""

PAGES = {
    "index.html": {
        "title": "Home",
        "content": """
        <section class="relative bg-primary text-white overflow-hidden py-32 lg:py-40">
            <div class="absolute inset-0 bg-gradient-to-br from-primary via-[#0f172a] to-[#0f172a] opacity-95 z-0"></div>
            <div class="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1555066931-4365d14bab8c?ixlib=rb-4.0.3')] bg-cover bg-center mix-blend-overlay z-0 opacity-40"></div>
            
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 flex flex-col justify-center items-center text-center min-h-[50vh]">
                <span class="inline-block py-1.5 px-5 rounded-full bg-secondary/20 border border-secondary/50 text-secondary font-bold text-sm mb-8 shadow-[0_0_15px_rgba(249,115,22,0.3)] backdrop-blur-sm" data-aos="fade-down">सीप सिकौँ, आत्मनिर्भर बनौँ!</span>
                <h1 class="text-5xl lg:text-7xl font-extrabold mb-6 leading-tight drop-shadow-lg" data-aos="fade-up" data-aos-delay="100">
                    Your Digital <br><span class="text-gradient"><span id="typed-text"></span></span>
                </h1>
                <p class="text-xl text-blue-100 max-w-3xl mb-12 leading-relaxed" data-aos="fade-up" data-aos-delay="200">
                    We build websites, create digital designs, improve online visibility, and provide practical digital skills to help individuals and businesses become digitally independent.
                </p>
                <div class="flex flex-wrap justify-center gap-5" data-aos="fade-up" data-aos-delay="300">
                    <a href="contact.html" class="bg-secondary text-white px-8 py-4 rounded-full font-bold hover:bg-orange-600 transition shadow-[0_0_20px_rgba(249,115,22,0.4)] hover:shadow-[0_0_30px_rgba(249,115,22,0.6)] hover:-translate-y-1 text-lg">Start Your Project</a>
                    <a href="training.html" class="bg-white/10 backdrop-blur-md border border-white/20 text-white px-8 py-4 rounded-full font-bold hover:bg-white hover:text-primary transition shadow-lg hover:-translate-y-1 text-lg">Join Training</a>
                </div>
            </div>
            <!-- Wave Divider -->
            <div class="wave-divider">
                <svg data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">
                    <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z" class="shape-fill"></path>
                </svg>
            </div>
        </section>

        <section class="py-24 bg-light relative">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
                <h2 class="text-sm font-bold text-secondary uppercase tracking-[0.2em] mb-3" data-aos="fade-up">Introduction</h2>
                <h3 class="text-4xl lg:text-5xl font-bold text-dark mb-10" data-aos="fade-up" data-aos-delay="100">Welcome to Db WebGraph</h3>
                <p class="text-lg text-slate-600 max-w-4xl mx-auto mb-16" data-aos="fade-up" data-aos-delay="200">
                    We provide complete digital solutions including Web Development, Graphic Design, SEO, Digital Branding, Basic Computer Training, Foundational Knowledge, and Practical Master Training.
                </p>
                
                <div class="bg-white p-10 lg:p-14 rounded-3xl border-l-4 border-secondary shadow-xl max-w-4xl mx-auto relative overflow-hidden group" data-aos="zoom-in" data-aos-delay="300">
                    <div class="absolute -top-10 -right-10 w-40 h-40 bg-orange-50 rounded-full opacity-50 group-hover:scale-[2] transition-transform duration-700"></div>
                    <i class="fas fa-quote-left absolute top-8 left-8 text-6xl text-slate-100 group-hover:text-orange-100 transition-colors duration-500"></i>
                    <p class="text-2xl lg:text-3xl font-medium text-primary leading-relaxed relative z-10 italic">
                        "We don't just create digital products for you; we help you learn how to create and manage them yourself."
                    </p>
                </div>
            </div>
        </section>
        
        <section class="py-24 bg-white relative">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center mb-20">
                    <h2 class="text-4xl lg:text-5xl font-bold text-dark mb-6" data-aos="fade-up">Why Choose Db WebGraph?</h2>
                    <div class="w-24 h-1.5 bg-gradient-to-r from-secondary to-orange-300 mx-auto rounded-full" data-aos="fade-up" data-aos-delay="100"></div>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
                    """ + "".join([
                        f"""
                        <div class="bg-slate-50 p-10 rounded-2xl shadow-sm border border-slate-100 card-hover icon-bounce relative overflow-hidden group" data-aos="fade-up" data-aos-delay="{delay}">
                            <div class="absolute -bottom-6 -right-6 w-24 h-24 bg-gradient-to-br from-transparent to-slate-200 rounded-full opacity-50 group-hover:scale-[4] transition-transform duration-700"></div>
                            <div class="w-16 h-16 bg-white rounded-xl shadow-md flex items-center justify-center mb-6 relative z-10 border border-slate-50">
                                <i class="{icon} text-3xl text-{color}"></i>
                            </div>
                            <h3 class="text-xl font-bold mb-3 relative z-10 text-dark">{title}</h3>
                            <p class="text-slate-600 relative z-10">{desc}</p>
                        </div>
                        """ for delay, icon, color, title, desc in [
                            ("100", "fas fa-tools", "secondary", "Practical", "Real-world and practical digital solutions designed for actual results."),
                            ("200", "fas fa-comments", "primary", "Simple", "Easy-to-understand communication and training, breaking down complex tech."),
                            ("300", "fas fa-briefcase", "secondary", "Professional", "Modern and professional digital services that elevate your brand."),
                            ("400", "fas fa-book-open", "primary", "Learning-Focused", "Clients can learn how to manage their own digital work independently."),
                            ("500", "fas fa-compress-arrows-alt", "secondary", "Flexible", "Solutions designed according to your specific individual or business needs."),
                            ("600", "fas fa-headset", "primary", "Long-Term Support", "Guidance for future updates, improvements, and continuous growth.")
                        ]
                    ]) + """
                </div>
            </div>
        </section>
        
        <section class="py-32 bg-dark text-center relative overflow-hidden">
            <div class="absolute inset-0 bg-gradient-to-b from-primary/60 to-dark z-0"></div>
            <div class="absolute top-0 right-0 w-[500px] h-[500px] bg-secondary/20 rounded-full blur-[120px] transform translate-x-1/2 -translate-y-1/2"></div>
            <div class="absolute bottom-0 left-0 w-[500px] h-[500px] bg-secondary/20 rounded-full blur-[120px] transform -translate-x-1/2 translate-y-1/2"></div>
            <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
                <h2 class="text-4xl lg:text-6xl font-extrabold text-white mb-8" data-aos="zoom-in">Have an Idea?<br>Let's Build It Together.</h2>
                <p class="text-xl text-slate-300 mb-12" data-aos="fade-up" data-aos-delay="100">
                    Do you have a digital idea, project, business, or skill you want to develop? Let's make it a reality.
                </p>
                <div class="flex justify-center gap-6 flex-wrap" data-aos="fade-up" data-aos-delay="200">
                    <a href="contact.html" class="bg-secondary text-white px-10 py-4 rounded-full font-bold hover:bg-orange-500 transition shadow-[0_0_20px_rgba(249,115,22,0.4)] hover:-translate-y-1 text-lg">Start a Project</a>
                    <a href="training.html" class="bg-white text-primary px-10 py-4 rounded-full font-bold hover:bg-slate-100 transition shadow-lg hover:-translate-y-1 text-lg">Join Training</a>
                </div>
            </div>
        </section>
        """
    },
    "about.html": {
        "title": "About Dharbindra BK",
        "content": """
        <section class="py-24 bg-light overflow-hidden">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <!-- Profile Section -->
                <div class="flex flex-col lg:flex-row gap-16 items-center mb-24">
                    <div class="w-full lg:w-1/3 relative" data-aos="fade-right">
                        <div class="absolute -inset-4 bg-gradient-to-br from-secondary/30 to-primary/30 rounded-3xl blur-lg z-0"></div>
                        <div class="relative rounded-3xl overflow-hidden shadow-2xl border-4 border-white bg-slate-100 aspect-square flex items-center justify-center z-10 group">
                            <i class="fas fa-user-tie text-[10rem] text-slate-300 group-hover:scale-110 transition-transform duration-500"></i>
                            <div class="absolute inset-0 bg-gradient-to-t from-dark/90 via-dark/40 to-transparent p-6 flex flex-col justify-end text-white text-center opacity-0 group-hover:opacity-100 transition-opacity duration-500">
                                <h2 class="text-3xl font-bold mb-1">Dharbindra BK</h2>
                                <p class="text-secondary font-medium">Founder</p>
                            </div>
                        </div>
                    </div>
                    <div class="w-full lg:w-2/3" data-aos="fade-left">
                        <h1 class="text-4xl lg:text-6xl font-extrabold text-dark mb-3">Dharbindra BK</h1>
                        <h2 class="text-xl lg:text-2xl text-secondary font-bold mb-8">Founder & Digital Skills Trainer — Db WebGraph</h2>
                        <p class="text-lg text-slate-600 mb-8 leading-relaxed">
                            Dharbindra BK is a web development and graphic design educator who focuses on teaching digital skills in a simple, practical, and student-friendly way. With a deep passion for empowering individuals, he bridges the gap between complex technology and accessible learning.
                        </p>
                        
                        <h3 class="text-lg font-bold text-primary mb-5">Areas of Work</h3>
                        <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                            """ + "".join([
                                f'<div class="bg-white p-5 rounded-xl text-center shadow-sm border border-slate-100 card-hover icon-bounce"><i class="{icon} text-3xl text-{color} mb-3 block"></i><span class="text-sm font-bold text-slate-700">{label}</span></div>'
                                for icon, color, label in [
                                    ("fas fa-code", "primary", "Web Dev"), ("fab fa-wordpress", "secondary", "WordPress"),
                                    ("fas fa-pen-nib", "primary", "Graphic Design"), ("fas fa-bullhorn", "secondary", "Digital Branding"),
                                    ("fas fa-search", "primary", "SEO"), ("fas fa-chalkboard-teacher", "secondary", "Online Learning"),
                                    ("fas fa-laptop", "primary", "Computer Edu"), ("fas fa-video", "secondary", "Content Creation")
                                ]
                            ]) + """
                        </div>
                    </div>
                </div>
                
                <!-- Timeline Section -->
                <div class="bg-white rounded-3xl shadow-xl p-10 lg:p-20 border border-slate-100" data-aos="fade-up">
                    <h2 class="text-3xl lg:text-4xl font-extrabold text-dark mb-16 text-center">More About Dharbindra BK</h2>
                    <div class="max-w-4xl mx-auto relative">
                        <!-- Vertical Line -->
                        <div class="hidden md:block absolute left-1/2 transform -translate-x-1/2 h-full w-1.5 bg-slate-100 rounded-full"></div>
                        
                        <div class="md:flex items-center justify-between mb-16 w-full relative" data-aos="fade-up" data-aos-delay="100">
                            <div class="md:w-5/12 mb-6 md:mb-0 md:text-right pr-0 md:pr-12">
                                <h3 class="text-2xl font-bold text-primary mb-3">The Vision</h3>
                                <p class="text-slate-600 text-lg">To create a platform where clients not only get premium digital services but also gain the practical knowledge to manage their own digital presence effectively.</p>
                            </div>
                            <div class="timeline-dot hidden md:block"></div>
                            <div class="md:w-5/12 pl-0 md:pl-12"></div>
                        </div>
                        
                        <div class="md:flex items-center justify-between mb-16 w-full flex-row-reverse relative" data-aos="fade-up" data-aos-delay="200">
                            <div class="md:w-5/12 mb-6 md:mb-0 pl-0 md:pl-12">
                                <h3 class="text-2xl font-bold text-primary mb-3">Teaching Philosophy</h3>
                                <p class="text-slate-600 text-lg">"Learn the Skill. Practice the Skill. Build Your Own Work." Education should be practical, straightforward, and immediately applicable in the real world.</p>
                            </div>
                            <div class="timeline-dot hidden md:block"></div>
                            <div class="md:w-5/12 pr-0 md:pr-12"></div>
                        </div>
                        
                        <div class="md:flex items-center justify-between w-full relative" data-aos="fade-up" data-aos-delay="300">
                            <div class="md:w-5/12 mb-6 md:mb-0 md:text-right pr-0 md:pr-12">
                                <h3 class="text-2xl font-bold text-primary mb-3">Future Goals</h3>
                                <p class="text-slate-600 text-lg">Expanding Db WebGraph to empower thousands of individuals across Nepal and globally to become digitally independent professionals.</p>
                            </div>
                            <div class="timeline-dot hidden md:block"></div>
                            <div class="md:w-5/12 pl-0 md:pl-12"></div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        """
    },
    "web-development.html": {
        "title": "Web Development",
        "content": """
        <section class="py-24 bg-slate-50">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center mb-20">
                    <h1 class="text-4xl lg:text-6xl font-extrabold text-dark mb-6" data-aos="fade-up">Web Development</h1>
                    <div class="w-24 h-1.5 bg-gradient-to-r from-secondary to-orange-300 mx-auto rounded-full mb-8" data-aos="fade-up" data-aos-delay="100"></div>
                    <p class="text-xl text-slate-600 max-w-2xl mx-auto" data-aos="fade-up" data-aos-delay="200">Build a professional digital presence for yourself, your organization, or your business.</p>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    """ + "".join([
                        f"""
                        <div class="bg-white p-8 rounded-3xl shadow-md border border-slate-100 flex flex-col card-hover icon-bounce relative overflow-hidden group" data-aos="fade-up" data-aos-delay="{delay}">
                            <div class="absolute -top-10 -right-10 w-40 h-40 bg-slate-50 rounded-full opacity-50 group-hover:scale-150 transition-transform duration-700"></div>
                            <i class="{icon} text-5xl text-primary mb-6 transition-colors group-hover:text-secondary relative z-10"></i>
                            <h3 class="text-2xl font-bold mb-4 relative z-10">{title}</h3>
                            <p class="text-slate-600 mb-6 flex-grow relative z-10">{desc}</p>
                            <div class="bg-orange-50/50 p-4 rounded-xl border border-orange-100 mt-auto relative z-10 group-hover:bg-orange-50 transition-colors">
                                <p class="text-sm text-secondary font-bold flex items-start"><i class="fas fa-graduation-cap mt-1 mr-2 text-lg"></i> We provide Master Training so you can operate it independently.</p>
                            </div>
                        </div>
                        """ for delay, icon, title, desc in [
                            ("100", "fas fa-id-card", "Portfolio Website", "Customized Portfolio Websites including Resume, Project Showcase, Personal Blog, and Creative Gallery to boost your personal brand."),
                            ("200", "fas fa-newspaper", "News Portal", "Professional News Portals to publish national news, sports, tech, and editorials. Organized efficiently for readers."),
                            ("300", "fas fa-shopping-cart", "E-commerce Website", "Manage physical products, digital services, subscriptions, and dropshipping easily with powerful e-commerce solutions."),
                            ("400", "fas fa-blog", "Personal Blog", "Share your passion for lifestyle, travel, food, tech, or photography with a beautifully designed personal blog."),
                            ("500", "fas fa-search-dollar", "SEO Optimization", "On-Page, Technical, Content, and Local SEO to improve search visibility and search engine ranking for your business."),
                            ("600", "fab fa-wordpress", "WordPress Services", "Complete WordPress development including themes, plugins, security, hosting setup, and maintenance. Fast & secure.")
                        ]
                    ]) + """
                </div>
            </div>
        </section>
        """
    },
    "graphic-design.html": {
        "title": "Graphic Design",
        "content": """
        <section class="py-24 bg-white relative overflow-hidden">
            <!-- Decorative BG -->
            <div class="absolute top-0 right-0 w-[800px] h-[800px] bg-slate-50 rounded-full -translate-y-1/2 translate-x-1/2 z-0"></div>
            
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
                <div class="text-center mb-20">
                    <h1 class="text-4xl lg:text-6xl font-extrabold text-dark mb-6" data-aos="fade-up">Graphic Design</h1>
                    <div class="w-24 h-1.5 bg-gradient-to-r from-secondary to-orange-300 mx-auto rounded-full mb-8" data-aos="fade-up" data-aos-delay="100"></div>
                    <p class="text-xl text-slate-600 max-w-2xl mx-auto" data-aos="fade-up" data-aos-delay="200">Creative design that gives your brand a highly professional and memorable identity.</p>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    """ + "".join([
                        f"""
                        <div class="bg-white p-8 rounded-3xl shadow-lg border border-slate-100 flex flex-col card-hover icon-bounce relative overflow-hidden group" data-aos="fade-up" data-aos-delay="{delay}">
                            <div class="absolute top-0 right-0 w-2 h-full bg-gradient-to-b from-primary to-secondary opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                            <div class="w-16 h-16 bg-slate-50 rounded-2xl flex items-center justify-center mb-6 shadow-sm border border-slate-100 group-hover:bg-primary group-hover:text-white transition-colors duration-300">
                                <i class="{icon} text-3xl text-secondary group-hover:text-white transition-colors"></i>
                            </div>
                            <h3 class="text-2xl font-bold mb-4">{title}</h3>
                            <p class="text-slate-600 mb-8 flex-grow">{desc}</p>
                            <div class="flex items-center text-sm font-bold text-primary group-hover:text-secondary transition-colors">
                                <i class="fas fa-graduation-cap mr-2 text-lg"></i> {training} Available
                            </div>
                        </div>
                        """ for delay, icon, title, desc, training in [
                            ("100", "fas fa-bezier-curve", "Logo & Branding", "Complete brand identity including logo design, business cards, letterheads, typography, and precise color schemes.", "Master Training"),
                            ("200", "fas fa-print", "Print & Web Graphics", "Eye-catching posters, flyers, banners, social media graphics, and infographics for digital and physical marketing.", "Practical Training"),
                            ("300", "fas fa-mobile-alt", "UI/UX Design", "Website and mobile app interface design, wireframes, prototypes, and complete user experience strategies.", "UI/UX Training"),
                            ("400", "fas fa-paint-brush", "Illustration & Vector", "Custom artwork, icons, cartoons, character design, and scalable vector illustrations tailored to your needs.", "Illustration Training"),
                            ("500", "fas fa-video", "Motion Graphics", "Engaging animated titles, explainer videos, social media video graphics, and smooth professional motion design.", "Motion Training"),
                            ("600", "fas fa-box-open", "Packaging Design", "Standout product packaging, labels, boxes, and product branding that appeals directly to your target customers.", "Packaging Training")
                        ]
                    ]) + """
                </div>
            </div>
        </section>
        """
    },
    "education.html": {
        "title": "Basic Computer & Foundational Knowledge",
        "content": """
        <section class="py-24 bg-slate-50">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center mb-20">
                <h1 class="text-4xl lg:text-6xl font-extrabold text-dark mb-6" data-aos="fade-up">Basic Computer & Foundation</h1>
                <div class="w-24 h-1.5 bg-gradient-to-r from-secondary to-orange-300 mx-auto rounded-full mb-8" data-aos="fade-up" data-aos-delay="100"></div>
                <p class="text-xl text-slate-600 max-w-3xl mx-auto" data-aos="fade-up" data-aos-delay="200">Build strong digital and academic foundations for everyday independence and professional growth.</p>
            </div>
            
            <div class="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-12">
                <!-- Basic Computer -->
                <div class="bg-white p-10 lg:p-14 rounded-3xl border-t-8 border-primary shadow-xl card-hover" data-aos="fade-right" data-aos-delay="300">
                    <div class="w-20 h-20 bg-blue-50 rounded-2xl flex items-center justify-center mb-8 shadow-inner">
                        <i class="fas fa-desktop text-4xl text-primary"></i>
                    </div>
                    <h3 class="text-3xl font-bold mb-6 text-dark">Basic Computer</h3>
                    <p class="text-slate-600 mb-8 text-lg leading-relaxed">Practical training designed to give you the confidence to manage daily computer tasks efficiently and safely.</p>
                    
                    <ul class="space-y-5 text-slate-700 font-medium">
                        <li class="flex items-center p-4 rounded-xl hover:bg-slate-50 transition"><div class="w-10 h-10 rounded-full bg-orange-50 flex items-center justify-center mr-4 shadow-sm"><i class="fas fa-check text-secondary"></i></div> Computer Fundamentals</li>
                        <li class="flex items-center p-4 rounded-xl hover:bg-slate-50 transition"><div class="w-10 h-10 rounded-full bg-orange-50 flex items-center justify-center mr-4 shadow-sm"><i class="fas fa-check text-secondary"></i></div> MS Word, Excel & PowerPoint</li>
                        <li class="flex items-center p-4 rounded-xl hover:bg-slate-50 transition"><div class="w-10 h-10 rounded-full bg-orange-50 flex items-center justify-center mr-4 shadow-sm"><i class="fas fa-check text-secondary"></i></div> Internet Browsing & Email</li>
                        <li class="flex items-center p-4 rounded-xl hover:bg-slate-50 transition"><div class="w-10 h-10 rounded-full bg-orange-50 flex items-center justify-center mr-4 shadow-sm"><i class="fas fa-check text-secondary"></i></div> File & Data Management</li>
                        <li class="flex items-center p-4 rounded-xl hover:bg-slate-50 transition"><div class="w-10 h-10 rounded-full bg-orange-50 flex items-center justify-center mr-4 shadow-sm"><i class="fas fa-check text-secondary"></i></div> Everyday Digital Skills</li>
                    </ul>
                </div>
                
                <!-- Foundational Knowledge -->
                <div class="bg-white p-10 lg:p-14 rounded-3xl border-t-8 border-secondary shadow-xl card-hover" data-aos="fade-left" data-aos-delay="400">
                    <div class="w-20 h-20 bg-orange-50 rounded-2xl flex items-center justify-center mb-8 shadow-inner">
                        <i class="fas fa-book-reader text-4xl text-secondary"></i>
                    </div>
                    <h3 class="text-3xl font-bold mb-6 text-dark">Foundational Knowledge</h3>
                    <p class="text-slate-600 mb-8 text-lg leading-relaxed">Strong foundational knowledge helps learners develop stronger academic logic and excellent professional skills.</p>
                    
                    <ul class="space-y-5 text-slate-700 font-medium">
                        <li class="flex items-center p-4 rounded-xl hover:bg-slate-50 transition"><div class="w-10 h-10 rounded-full bg-blue-50 flex items-center justify-center mr-4 shadow-sm"><i class="fas fa-check text-primary"></i></div> Mathematics & Logic</li>
                        <li class="flex items-center p-4 rounded-xl hover:bg-slate-50 transition"><div class="w-10 h-10 rounded-full bg-blue-50 flex items-center justify-center mr-4 shadow-sm"><i class="fas fa-check text-primary"></i></div> English Grammar & Writing</li>
                        <li class="flex items-center p-4 rounded-xl hover:bg-slate-50 transition"><div class="w-10 h-10 rounded-full bg-blue-50 flex items-center justify-center mr-4 shadow-sm"><i class="fas fa-check text-primary"></i></div> Nepali Grammar</li>
                        <li class="flex items-center p-4 rounded-xl hover:bg-slate-50 transition"><div class="w-10 h-10 rounded-full bg-blue-50 flex items-center justify-center mr-4 shadow-sm"><i class="fas fa-check text-primary"></i></div> Basic Digital Literacy</li>
                    </ul>
                </div>
            </div>
            
            <div class="mt-20 text-center" data-aos="zoom-in" data-aos-delay="500">
                <a href="training.html" class="bg-primary text-white px-10 py-5 rounded-full font-bold hover:bg-blue-800 transition shadow-xl text-xl btn-glow inline-block">Join a Training Program</a>
            </div>
        </section>
        """
    },
    "training.html": {
        "title": "Master Training",
        "content": """
        <section class="py-24 bg-white relative">
            <div class="absolute top-0 right-0 w-full h-96 bg-slate-50 -skew-y-3 origin-top-left z-0"></div>
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center mb-20 relative z-10">
                <h1 class="text-4xl lg:text-6xl font-extrabold text-dark mb-4" data-aos="fade-up">Master Training</h1>
                <p class="text-2xl md:text-3xl text-secondary font-bold max-w-3xl mx-auto mb-8 drop-shadow-sm" data-aos="fade-up" data-aos-delay="100">Learn the Skill. Practice the Skill. Build Your Own Work.</p>
                <p class="text-xl text-slate-600 max-w-2xl mx-auto" data-aos="fade-up" data-aos-delay="200">Db WebGraph provides practical, hands-on training tailored for individuals who want to become completely self-reliant.</p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6 relative z-10">
                """ + "".join([
                    f"""
                    <div class="bg-white rounded-2xl overflow-hidden shadow-lg border border-slate-100 flex flex-col card-hover" data-aos="fade-up" data-aos-delay="{delay}">
                        <div class="p-8 flex-grow border-b border-slate-100 relative overflow-hidden group">
                            <div class="absolute -right-4 -top-4 w-16 h-16 bg-slate-50 rounded-full group-hover:scale-[5] transition-transform duration-500 z-0"></div>
                            <div class="w-12 h-12 bg-orange-50 rounded-lg flex items-center justify-center mb-5 relative z-10 border border-orange-100">
                                <i class="{icon} text-2xl text-secondary"></i>
                            </div>
                            <h3 class="text-xl font-bold mb-3 text-primary relative z-10">{title}</h3>
                            <p class="text-slate-600 text-sm mb-5 relative z-10 leading-relaxed">{desc}</p>
                            <div class="space-y-2 text-sm text-slate-500 font-semibold relative z-10">
                                <p class="flex items-center"><i class="fas fa-layer-group w-6 text-secondary"></i> All Levels</p>
                                <p class="flex items-center"><i class="fas fa-clock w-6 text-secondary"></i> Flexible Duration</p>
                                <p class="flex items-center"><i class="fas fa-laptop-house w-6 text-secondary"></i> Online / Offline</p>
                            </div>
                        </div>
                        <div class="p-4 bg-slate-50">
                            <a href="contact.html" class="block w-full text-center bg-white border-2 border-primary text-primary py-2.5 rounded-lg font-bold hover:bg-primary hover:text-white transition shadow-sm">Enroll Now</a>
                        </div>
                    </div>
                    """ for delay, icon, title, desc in [
                        ("100", "fas fa-code", "Web Development", "Learn to build responsive professional websites from scratch."),
                        ("150", "fab fa-wordpress", "WordPress Master", "Complete practical training on WordPress CMS management."),
                        ("200", "fas fa-pen-nib", "Graphic Design", "Master modern design principles and professional tools."),
                        ("250", "fas fa-mobile-alt", "UI/UX Design", "Learn to create stunning and user-friendly digital interfaces."),
                        ("300", "fas fa-search", "SEO Training", "Optimize websites effectively for better search engine ranking."),
                        ("350", "fas fa-desktop", "Basic Computer", "Essential computer skills for everyday independence and tasks."),
                        ("400", "fas fa-bullhorn", "Digital Branding", "Create and manage brand identity across online platforms."),
                        ("450", "fas fa-robot", "AI Content Creation", "Leverage modern AI tools for massive content generation."),
                        ("500", "fas fa-calculator", "Mathematics", "Foundational mathematics for logic and problem-solving."),
                        ("550", "fas fa-spell-check", "English Grammar", "Improve communication and strictly professional writing."),
                        ("600", "fas fa-language", "Nepali Grammar", "Strengthen foundational language and expression skills."),
                        ("650", "fas fa-wifi", "Digital Literacy", "Basic knowledge to navigate the internet world securely.")
                    ]
                ]) + """
            </div>
            
            <div class="text-center mt-20" data-aos="zoom-in" data-aos-delay="300">
                <div class="bg-gradient-to-r from-primary to-blue-900 p-12 rounded-3xl max-w-5xl mx-auto shadow-2xl relative overflow-hidden">
                    <div class="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&w=2000&q=80')] opacity-10 bg-cover bg-center mix-blend-overlay"></div>
                    <h3 class="text-3xl lg:text-4xl font-bold text-white mb-6 relative z-10">Ready to gain practical digital skills?</h3>
                    <p class="text-blue-100 mb-8 text-lg relative z-10 max-w-2xl mx-auto">Join our intensive master training programs and take absolute control over your digital future.</p>
                    <a href="contact.html" class="bg-secondary text-white px-10 py-4 rounded-full font-bold text-xl hover:bg-orange-500 transition shadow-[0_0_20px_rgba(249,115,22,0.5)] inline-block relative z-10 hover:-translate-y-1">Start Learning Today</a>
                </div>
            </div>
        </section>
        """
    },
    "portfolio.html": {
        "title": "Portfolio",
        "content": """
        <section class="py-24 bg-slate-50">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center mb-16">
                    <h1 class="text-4xl lg:text-6xl font-extrabold text-dark mb-6" data-aos="fade-up">Our Portfolio</h1>
                    <div class="w-24 h-1.5 bg-gradient-to-r from-secondary to-orange-300 mx-auto rounded-full mb-8" data-aos="fade-up" data-aos-delay="100"></div>
                    <p class="text-xl text-slate-600 max-w-2xl mx-auto" data-aos="fade-up" data-aos-delay="200">Explore some of our recent digital projects and stunning creations.</p>
                </div>
                
                <!-- Filters -->
                <div class="flex flex-wrap justify-center gap-4 mb-16" data-aos="fade-up" data-aos-delay="300">
                    <button class="px-6 py-2.5 rounded-full bg-primary text-white font-bold text-sm shadow-md hover:bg-blue-800 transition">All Projects</button>
                    <button class="px-6 py-2.5 rounded-full bg-white border border-slate-200 text-slate-600 font-bold text-sm hover:border-secondary hover:text-secondary shadow-sm transition">Websites</button>
                    <button class="px-6 py-2.5 rounded-full bg-white border border-slate-200 text-slate-600 font-bold text-sm hover:border-secondary hover:text-secondary shadow-sm transition">Logo & Branding</button>
                    <button class="px-6 py-2.5 rounded-full bg-white border border-slate-200 text-slate-600 font-bold text-sm hover:border-secondary hover:text-secondary shadow-sm transition">UI/UX</button>
                    <button class="px-6 py-2.5 rounded-full bg-white border border-slate-200 text-slate-600 font-bold text-sm hover:border-secondary hover:text-secondary shadow-sm transition">Print Design</button>
                </div>

                <div class="columns-1 md:columns-2 lg:columns-3 gap-8 space-y-8">
                    """ + "".join([
                        f"""
                        <div class="break-inside-avoid relative rounded-2xl overflow-hidden group shadow-lg bg-white" data-aos="zoom-in" data-aos-delay="{delay}">
                            <div class="aspect-auto overflow-hidden">
                                <img src="{img}" alt="Project" class="w-full h-auto object-cover transition-transform duration-700 group-hover:scale-110">
                            </div>
                            <div class="absolute inset-0 bg-gradient-to-t from-dark via-dark/50 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 flex flex-col justify-end p-8">
                                <span class="text-secondary text-sm font-extrabold uppercase tracking-widest mb-2 transform translate-y-4 group-hover:translate-y-0 transition-transform duration-500">{cat}</span>
                                <h3 class="text-white text-2xl font-bold mb-4 transform translate-y-4 group-hover:translate-y-0 transition-transform duration-500 delay-75">{title}</h3>
                                <a href="#" class="inline-block px-5 py-2.5 bg-secondary text-white rounded-lg text-sm font-bold hover:bg-white hover:text-primary transition shadow-md w-max transform translate-y-4 group-hover:translate-y-0 transition-transform duration-500 delay-100">View Project</a>
                            </div>
                        </div>
                        """ for delay, img, cat, title in [
                            ("100", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=600&q=80", "Website", "Corporate Business Portal"),
                            ("200", "https://images.unsplash.com/photo-1626785774573-4b799315345d?auto=format&fit=crop&w=600&q=80", "Branding", "Modern Logo Identity"),
                            ("300", "https://images.unsplash.com/photo-1561070791-2526d30994b5?auto=format&fit=crop&w=600&q=80", "UI/UX", "Mobile App Interface"),
                            ("400", "https://images.unsplash.com/photo-1558655146-d09347e92766?auto=format&fit=crop&w=600&q=80", "Web Development", "E-Commerce Platform"),
                            ("500", "https://images.unsplash.com/photo-1626785774625-ddcddc3445e9?auto=format&fit=crop&w=600&q=80", "Print Design", "Magazine Cover Layout"),
                            ("600", "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=600&q=80", "WordPress", "Personal News Blog")
                        ]
                    ]) + """
                </div>
            </div>
        </section>
        """
    },
    "blog.html": {
        "title": "Blog & Articles",
        "content": """
        <section class="py-24 bg-white relative">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center mb-20">
                    <h1 class="text-4xl lg:text-6xl font-extrabold text-dark mb-6" data-aos="fade-up">Blog & Articles</h1>
                    <div class="w-24 h-1.5 bg-gradient-to-r from-secondary to-orange-300 mx-auto rounded-full mb-8" data-aos="fade-up" data-aos-delay="100"></div>
                    <p class="text-xl text-slate-600 max-w-2xl mx-auto" data-aos="fade-up" data-aos-delay="200">Insights, tutorials, and updates on digital skills to keep you learning.</p>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
                    """ + "".join([
                        f"""
                        <div class="bg-white rounded-3xl overflow-hidden border border-slate-100 shadow-lg card-hover flex flex-col group" data-aos="fade-up" data-aos-delay="{delay}">
                            <div class="h-56 bg-slate-200 relative overflow-hidden">
                                <img src="{img}" alt="Blog Image" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
                                <div class="absolute inset-0 bg-gradient-to-t from-dark/60 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                                <div class="absolute top-4 left-4 bg-secondary text-white text-xs font-bold px-3 py-1.5 rounded-md uppercase tracking-wider shadow-md">{cat}</div>
                            </div>
                            <div class="p-8 flex-grow flex flex-col">
                                <h3 class="text-2xl font-bold text-dark mb-4 group-hover:text-primary transition-colors cursor-pointer leading-snug">{title}</h3>
                                <p class="text-slate-600 text-sm mb-6 flex-grow leading-relaxed">Learn the essential skills to improve your digital independence. We break down the complex aspects into easy-to-understand tutorials...</p>
                                <div class="flex items-center justify-between border-t border-slate-100 pt-5 mt-auto">
                                    <span class="text-xs text-slate-500 font-bold uppercase tracking-wider"><i class="far fa-calendar-alt mr-2 text-secondary"></i> Oct 24, 2026</span>
                                    <a href="#" class="text-sm font-bold text-primary hover:text-secondary transition flex items-center">Read More <i class="fas fa-arrow-right ml-2 transition-transform group-hover:translate-x-1"></i></a>
                                </div>
                            </div>
                        </div>
                        """ for delay, img, cat, title in [
                            ("100", "https://images.unsplash.com/photo-1499951360447-b19be8fe80f5?auto=format&fit=crop&w=500&q=80", "Web Development", "How to Manage Your Own WordPress Site Effectively"),
                            ("200", "https://images.unsplash.com/photo-1542744094-3a31f272c490?auto=format&fit=crop&w=500&q=80", "SEO", "5 Simple SEO Tricks for Local Businesses to Rank Higher"),
                            ("300", "https://images.unsplash.com/photo-1626785774573-4b799315345d?auto=format&fit=crop&w=500&q=80", "Design", "Why Branding Matters More Than Just a Logo Design"),
                            ("400", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=500&q=80", "Computer Education", "Digital Literacy: Navigating the Internet Safely"),
                            ("500", "https://images.unsplash.com/photo-1501504905252-473c47e087f8?auto=format&fit=crop&w=500&q=80", "Tutorials", "Getting Started with Basic HTML & CSS for Beginners"),
                            ("600", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=500&q=80", "Digital Business", "How to Take Your Physical Business Online in 2026")
                        ]
                    ]) + """
                </div>
            </div>
        </section>
        """
    },
    "contact.html": {
        "title": "Contact Us",
        "content": """
        <section class="py-24 bg-slate-50 relative overflow-hidden">
            <!-- Decorative circle -->
            <div class="absolute top-0 left-0 w-[600px] h-[600px] bg-primary/5 rounded-full blur-[100px] -translate-x-1/2 -translate-y-1/2"></div>
            
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
                <div class="text-center mb-16">
                    <h1 class="text-4xl lg:text-6xl font-extrabold text-dark mb-6" data-aos="fade-up">Let's Build Your Digital Identity</h1>
                    <div class="w-24 h-1.5 bg-gradient-to-r from-secondary to-orange-300 mx-auto rounded-full mb-8" data-aos="fade-up" data-aos-delay="100"></div>
                    <p class="text-xl text-slate-600 max-w-2xl mx-auto" data-aos="fade-up" data-aos-delay="200">Get in touch to start a project or join our practical training sessions today.</p>
                </div>
                
                <div class="flex flex-col lg:flex-row gap-0 bg-white rounded-3xl shadow-2xl overflow-hidden border border-slate-100" data-aos="fade-up" data-aos-delay="300">
                    <!-- Contact Info Panel -->
                    <div class="w-full lg:w-2/5 bg-primary p-12 lg:p-16 text-white flex flex-col justify-between relative overflow-hidden">
                        <div class="absolute top-0 right-0 w-80 h-80 bg-secondary opacity-20 rounded-full blur-[60px] transform translate-x-1/3 -translate-y-1/3"></div>
                        <div class="absolute bottom-0 left-0 w-80 h-80 bg-blue-500 opacity-20 rounded-full blur-[60px] transform -translate-x-1/3 translate-y-1/3"></div>
                        
                        <div class="relative z-10">
                            <h2 class="text-3xl font-extrabold mb-4">Contact Info</h2>
                            <p class="text-blue-200 mb-12 text-lg leading-relaxed">We would love to hear from you. Fill out the form or use the information below to connect with us directly.</p>
                            
                            <div class="space-y-8">
                                <div class="flex items-center gap-6 group cursor-pointer">
                                    <div class="w-14 h-14 bg-blue-800 rounded-full flex items-center justify-center text-secondary text-2xl group-hover:bg-secondary group-hover:text-white transition-colors shadow-lg"><i class="fas fa-map-marker-alt"></i></div>
                                    <div>
                                        <h4 class="font-bold text-sm text-blue-300 uppercase tracking-wider mb-1">Location</h4>
                                        <p class="text-lg font-medium group-hover:text-secondary transition-colors">Kathmandu, Nepal</p>
                                    </div>
                                </div>
                                <div class="flex items-center gap-6 group cursor-pointer">
                                    <div class="w-14 h-14 bg-blue-800 rounded-full flex items-center justify-center text-secondary text-2xl group-hover:bg-secondary group-hover:text-white transition-colors shadow-lg"><i class="fas fa-phone-alt"></i></div>
                                    <div>
                                        <h4 class="font-bold text-sm text-blue-300 uppercase tracking-wider mb-1">Phone & WhatsApp</h4>
                                        <p class="text-lg font-medium group-hover:text-secondary transition-colors">+977 9800000000</p>
                                    </div>
                                </div>
                                <div class="flex items-center gap-6 group cursor-pointer">
                                    <div class="w-14 h-14 bg-blue-800 rounded-full flex items-center justify-center text-secondary text-2xl group-hover:bg-secondary group-hover:text-white transition-colors shadow-lg"><i class="fas fa-envelope"></i></div>
                                    <div>
                                        <h4 class="font-bold text-sm text-blue-300 uppercase tracking-wider mb-1">Email Address</h4>
                                        <p class="text-lg font-medium group-hover:text-secondary transition-colors">contact@dbwebgraph.com</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <div class="mt-16 relative z-10">
                            <h4 class="font-bold mb-6 text-blue-300 uppercase tracking-wider">Follow Us</h4>
                            <div class="flex space-x-4">
                                <a href="#" class="w-12 h-12 rounded-full bg-blue-800 flex items-center justify-center hover:bg-secondary transition transform hover:-translate-y-1 shadow-lg text-lg"><i class="fab fa-facebook-f"></i></a>
                                <a href="#" class="w-12 h-12 rounded-full bg-blue-800 flex items-center justify-center hover:bg-secondary transition transform hover:-translate-y-1 shadow-lg text-lg"><i class="fab fa-youtube"></i></a>
                                <a href="#" class="w-12 h-12 rounded-full bg-blue-800 flex items-center justify-center hover:bg-secondary transition transform hover:-translate-y-1 shadow-lg text-lg"><i class="fab fa-tiktok"></i></a>
                                <a href="#" class="w-12 h-12 rounded-full bg-blue-800 flex items-center justify-center hover:bg-secondary transition transform hover:-translate-y-1 shadow-lg text-lg"><i class="fab fa-linkedin-in"></i></a>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Form Panel -->
                    <div class="w-full lg:w-3/5 p-12 lg:p-16 bg-white">
                        <h3 class="text-2xl font-bold text-dark mb-8">Send us a message</h3>
                        <form class="space-y-8">
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                                <div class="relative">
                                    <label class="block text-sm font-bold text-slate-700 mb-2">Full Name</label>
                                    <input type="text" class="w-full px-5 py-4 bg-slate-50 rounded-xl border-transparent focus:bg-white focus:border-secondary focus:ring-2 focus:ring-secondary/20 outline-none transition shadow-sm" placeholder="John Doe">
                                </div>
                                <div class="relative">
                                    <label class="block text-sm font-bold text-slate-700 mb-2">Email Address</label>
                                    <input type="email" class="w-full px-5 py-4 bg-slate-50 rounded-xl border-transparent focus:bg-white focus:border-secondary focus:ring-2 focus:ring-secondary/20 outline-none transition shadow-sm" placeholder="john@example.com">
                                </div>
                            </div>
                            
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                                <div class="relative">
                                    <label class="block text-sm font-bold text-slate-700 mb-2">Phone Number</label>
                                    <input type="tel" class="w-full px-5 py-4 bg-slate-50 rounded-xl border-transparent focus:bg-white focus:border-secondary focus:ring-2 focus:ring-secondary/20 outline-none transition shadow-sm" placeholder="+977 98XXXXXXX">
                                </div>
                                <div class="relative">
                                    <label class="block text-sm font-bold text-slate-700 mb-2">Select Service</label>
                                    <select class="w-full px-5 py-4 bg-slate-50 rounded-xl border-transparent focus:bg-white focus:border-secondary focus:ring-2 focus:ring-secondary/20 outline-none transition shadow-sm appearance-none cursor-pointer">
                                        <option value="">Choose a service...</option>
                                        <option>Portfolio Website</option>
                                        <option>News Portal</option>
                                        <option>E-commerce Website</option>
                                        <option>Personal Blog</option>
                                        <option>SEO</option>
                                        <option>Graphic Design</option>
                                        <option>Logo & Branding</option>
                                        <option>UI/UX Design</option>
                                        <option>Motion Graphics</option>
                                        <option>Packaging Design</option>
                                        <option>Training</option>
                                        <option>Other</option>
                                    </select>
                                    <i class="fas fa-chevron-down absolute right-5 top-12 text-slate-400 pointer-events-none"></i>
                                </div>
                            </div>
                            
                            <div class="relative">
                                <label class="block text-sm font-bold text-slate-700 mb-2">Budget (Optional)</label>
                                <input type="text" class="w-full px-5 py-4 bg-slate-50 rounded-xl border-transparent focus:bg-white focus:border-secondary focus:ring-2 focus:ring-secondary/20 outline-none transition shadow-sm" placeholder="Your estimated budget">
                            </div>
                            
                            <div class="relative">
                                <label class="block text-sm font-bold text-slate-700 mb-2">Message</label>
                                <textarea rows="5" class="w-full px-5 py-4 bg-slate-50 rounded-xl border-transparent focus:bg-white focus:border-secondary focus:ring-2 focus:ring-secondary/20 outline-none transition shadow-sm resize-none" placeholder="Tell us about your project or training needs..."></textarea>
                            </div>
                            
                            <div class="flex gap-4 pt-4">
                                <button type="button" class="bg-primary text-white px-10 py-4 rounded-xl font-bold hover:bg-blue-800 transition shadow-lg w-full sm:w-auto btn-glow text-lg">Send Inquiry</button>
                                <button type="button" class="bg-white border-2 border-slate-200 text-slate-700 px-10 py-4 rounded-xl font-bold hover:border-primary hover:text-primary transition w-full sm:w-auto shadow-sm text-lg">Request Consultation</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </section>
        """
    }
}

for filename, data in PAGES.items():
    filepath = os.path.join(WORKSPACE, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(HEADER.replace('{title}', data['title']) + data['content'] + FOOTER)

print("Site generation complete!")
