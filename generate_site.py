import os

WORKSPACE = r"c:\Users\A C E R\OneDrive\Desktop\Db WebGraphsit"
os.makedirs(WORKSPACE, exist_ok=True)

HEADER = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Db WebGraph</title>
    
    <!-- SEO & Meta Tags -->
    <meta name="description" content="Db WebGraph is your digital identity partner, offering premium Web Development, Graphic Design, SEO, and practical Digital Skills Training.">
    <meta name="keywords" content="Web Development, Graphic Design, Digital Agency, SEO, Computer Training, Nepal, Dharbindra BK">
    <meta name="author" content="Dharbindra BK">
    
    <!-- Schema.org for LocalBusiness/Organization -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "ProfessionalService",
      "name": "Db WebGraph",
      "image": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=800&q=80",
      "description": "We build websites, create digital designs, improve online visibility, and provide practical digital skills.",
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Kathmandu",
        "addressCountry": "NP"
      },
      "telephone": "+977-9800000000",
      "url": "https://dbwebgraph.vercel.app"
    }
    </script>

    <!-- Preconnect for performance -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preconnect" href="https://cdn.tailwindcss.com">

    <!-- Fonts: Space Grotesk & Inter -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    
    <!-- Icons -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    fontFamily: { 
                        sans: ['Inter', 'sans-serif'],
                        display: ['Space Grotesk', 'sans-serif']
                    },
                    colors: {
                        primary: '#0a0a0a',
                        secondary: '#171717',
                        accent: {
                            DEFAULT: '#f97316',
                            glow: 'rgba(249, 115, 22, 0.5)'
                        },
                        brand: {
                            blue: '#3b82f6',
                            purple: '#8b5cf6'
                        }
                    },
                    animation: {
                        'float': 'float 6s ease-in-out infinite',
                        'float-delayed': 'float 6s ease-in-out 2s infinite',
                        'blob': 'blob 15s infinite alternate',
                    },
                    keyframes: {
                        float: {
                            '0%, 100%': { transform: 'translateY(0)' },
                            '50%': { transform: 'translateY(-20px)' },
                        },
                        blob: {
                            '0%': { transform: 'translate(0px, 0px) scale(1)' },
                            '33%': { transform: 'translate(50px, -50px) scale(1.1)' },
                            '66%': { transform: 'translate(-40px, 40px) scale(0.9)' },
                            '100%': { transform: 'translate(0px, 0px) scale(1)' },
                        }
                    }
                }
            }
        }
    </script>
    
    <style>
        :root {
            --glass-bg: rgba(23, 23, 23, 0.6);
            --glass-border: rgba(255, 255, 255, 0.08);
        }

        body {
            background-color: #050505;
            color: #e5e5e5;
            overflow-x: hidden;
        }

        ::-webkit-scrollbar { width: 8px; }
        ::-webkit-scrollbar-track { background: #0a0a0a; }
        ::-webkit-scrollbar-thumb { background: #333; border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: #f97316; }

        .glass {
            background: var(--glass-bg);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid var(--glass-border);
        }
        
        .glass-card {
            background: linear-gradient(145deg, rgba(30,30,30,0.4) 0%, rgba(15,15,15,0.4) 100%);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 24px;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .glass-card:hover {
            border-color: rgba(249, 115, 22, 0.3);
            box-shadow: 0 10px 40px -10px rgba(249, 115, 22, 0.15);
            transform: translateY(-5px);
        }

        .glow-text { text-shadow: 0 0 25px rgba(249, 115, 22, 0.5); }
        .text-gradient { background: linear-gradient(135deg, #ffffff 0%, #a3a3a3 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .text-gradient-accent { background: linear-gradient(135deg, #f97316 0%, #fb923c 50%, #fcd34d 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }

        .btn-primary {
            background: linear-gradient(135deg, #f97316, #ea580c);
            color: white;
            box-shadow: 0 4px 15px rgba(249, 115, 22, 0.3), inset 0 1px 0 rgba(255,255,255,0.2);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
            border: 1px solid transparent;
        }
        
        .btn-primary::after {
            content: ''; position: absolute; top: 0; left: -100%; width: 100%; height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
            transition: all 0.5s ease;
        }
        .btn-primary:hover::after { left: 100%; }
        .btn-primary:hover {
            box-shadow: 0 8px 25px rgba(249, 115, 22, 0.5);
            transform: translateY(-2px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .btn-secondary {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: white;
            backdrop-filter: blur(10px);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .btn-secondary:hover {
            background: rgba(255, 255, 255, 0.08);
            border-color: rgba(255, 255, 255, 0.25);
            transform: translateY(-2px);
        }

        .shape-blob { position: absolute; filter: blur(90px); z-index: -1; opacity: 0.4; border-radius: 50%; }
        .reveal { opacity: 0; transform: translateY(30px); transition: all 0.8s cubic-bezier(0.5, 0, 0, 1); }
        .reveal.active { opacity: 1; transform: translateY(0); }
    </style>
</head>
<body class="antialiased selection:bg-accent selection:text-white">

    <div class="fixed inset-0 overflow-hidden pointer-events-none z-[-1]">
        <div class="shape-blob bg-brand-purple/20 w-[300px] h-[300px] md:w-[500px] md:h-[500px] top-[-10%] left-[-10%] animate-blob"></div>
        <div class="shape-blob bg-accent/20 w-[250px] h-[250px] md:w-[400px] md:h-[400px] top-[40%] right-[-5%] animate-blob" style="animation-delay: -5s;"></div>
        <div class="shape-blob bg-brand-blue/20 w-[400px] h-[400px] md:w-[600px] md:h-[600px] bottom-[-20%] left-[20%] animate-blob" style="animation-delay: -10s;"></div>
    </div>

    <!-- Navigation -->
    <nav id="navbar" class="fixed w-full top-0 z-50 transition-all duration-300 border-b border-transparent">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-20">
                <a href="index.html" class="flex-shrink-0 flex items-center gap-3 group" aria-label="Db WebGraph Home">
                    <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-accent to-orange-500 flex items-center justify-center shadow-lg shadow-accent/20 group-hover:shadow-accent/40 transition-all duration-300 transform group-hover:scale-105">
                        <i class="fas fa-layer-group text-white text-xl"></i>
                    </div>
                    <span class="font-display font-bold text-xl tracking-tight text-white group-hover:text-gray-200 transition-colors">Db WebGraph</span>
                </a>
                <div class="hidden lg:flex items-center space-x-1 glass px-6 py-2 rounded-full shadow-lg shadow-black/20">
                    <a href="index.html" class="px-4 py-2 text-sm font-medium text-white bg-white/10 rounded-full transition-all">Home</a>
                    <a href="about.html" class="px-4 py-2 text-sm font-medium text-gray-400 hover:text-white hover:bg-white/5 rounded-full transition-all">About</a>
                    <a href="web-development.html" class="px-4 py-2 text-sm font-medium text-gray-400 hover:text-white hover:bg-white/5 rounded-full transition-all">Services</a>
                    <a href="portfolio.html" class="px-4 py-2 text-sm font-medium text-gray-400 hover:text-white hover:bg-white/5 rounded-full transition-all">Portfolio</a>
                    <a href="training.html" class="px-4 py-2 text-sm font-medium text-gray-400 hover:text-white hover:bg-white/5 rounded-full transition-all">Training</a>
                </div>
                <div class="flex items-center gap-4">
                    <a href="contact.html" class="hidden md:inline-flex btn-primary px-6 py-2.5 rounded-full font-medium text-sm shadow-lg">Start Project</a>
                    <button id="mobile-menu-btn" class="lg:hidden p-2 text-gray-300 hover:text-white focus:outline-none" aria-label="Toggle Menu">
                        <div class="w-6 h-5 flex flex-col justify-between relative">
                            <span class="w-full h-0.5 bg-current transform transition-all duration-300 origin-left"></span>
                            <span class="w-full h-0.5 bg-current transform transition-all duration-300"></span>
                            <span class="w-full h-0.5 bg-current transform transition-all duration-300 origin-left"></span>
                        </div>
                    </button>
                </div>
            </div>
        </div>
        <!-- Mobile Menu -->
        <div id="mobile-menu" class="hidden lg:hidden glass border-t border-white/10 absolute w-full left-0 origin-top animate-fade-in-down shadow-2xl">
            <div class="px-6 py-8 flex flex-col space-y-5">
                <a href="index.html" class="text-lg font-display font-medium text-white hover:text-accent transition-colors">Home</a>
                <a href="about.html" class="text-lg font-display font-medium text-gray-300 hover:text-accent transition-colors">About</a>
                <a href="web-development.html" class="text-lg font-display font-medium text-gray-300 hover:text-accent transition-colors">Services</a>
                <a href="portfolio.html" class="text-lg font-display font-medium text-gray-300 hover:text-accent transition-colors">Portfolio</a>
                <a href="training.html" class="text-lg font-display font-medium text-gray-300 hover:text-accent transition-colors">Training</a>
                <a href="contact.html" class="btn-primary text-center px-6 py-3 rounded-xl font-medium">Start Project</a>
            </div>
        </div>
    </nav>
    <main class="flex-grow pt-20">
"""

FOOTER = """
    </main>
    
    <!-- Footer -->
    <footer class="border-t border-white/10 bg-[#050505] pt-24 pb-12 relative overflow-hidden mt-20">
        <div class="absolute bottom-0 left-1/2 -translate-x-1/2 w-3/4 h-1/2 bg-accent/5 blur-[120px] pointer-events-none rounded-full"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 lg:gap-16 mb-16">
                <div class="col-span-1 lg:col-span-1">
                    <a href="index.html" class="flex items-center gap-3 mb-8 group" aria-label="Db WebGraph Home">
                        <div class="w-10 h-10 rounded-xl bg-accent flex items-center justify-center transform group-hover:scale-105 transition-transform">
                            <i class="fas fa-layer-group text-white text-lg"></i>
                        </div>
                        <span class="font-display font-bold text-2xl text-white tracking-tight">Db WebGraph</span>
                    </a>
                    <p class="text-gray-400 text-sm leading-relaxed mb-8 pr-4">
                        Your Digital Identity Partner. Professional services combined with practical learning to make you digitally independent.
                    </p>
                    <div class="flex space-x-4">
                        <a href="#" class="w-11 h-11 rounded-full glass border-white/10 flex items-center justify-center text-gray-400 hover:text-white hover:border-accent hover:bg-accent/20 transition-all duration-300"><i class="fab fa-facebook-f"></i></a>
                        <a href="#" class="w-11 h-11 rounded-full glass border-white/10 flex items-center justify-center text-gray-400 hover:text-white hover:border-accent hover:bg-accent/20 transition-all duration-300"><i class="fab fa-linkedin-in"></i></a>
                        <a href="#" class="w-11 h-11 rounded-full glass border-white/10 flex items-center justify-center text-gray-400 hover:text-white hover:border-accent hover:bg-accent/20 transition-all duration-300"><i class="fab fa-youtube"></i></a>
                    </div>
                </div>
                
                <div>
                    <h3 class="font-display font-bold text-white text-lg mb-6 tracking-wide">Services</h3>
                    <ul class="space-y-4 text-sm text-gray-400 font-medium">
                        <li><a href="web-development.html" class="hover:text-accent transition-colors flex items-center gap-2 group"><i class="fas fa-angle-right text-xs text-gray-600 group-hover:text-accent"></i> Web Development</a></li>
                        <li><a href="graphic-design.html" class="hover:text-accent transition-colors flex items-center gap-2 group"><i class="fas fa-angle-right text-xs text-gray-600 group-hover:text-accent"></i> Graphic Design</a></li>
                        <li><a href="training.html" class="hover:text-accent transition-colors flex items-center gap-2 group"><i class="fas fa-angle-right text-xs text-gray-600 group-hover:text-accent"></i> Master Training</a></li>
                    </ul>
                </div>
                
                <div>
                    <h3 class="font-display font-bold text-white text-lg mb-6 tracking-wide">Company</h3>
                    <ul class="space-y-4 text-sm text-gray-400 font-medium">
                        <li><a href="about.html" class="hover:text-accent transition-colors flex items-center gap-2 group"><i class="fas fa-angle-right text-xs text-gray-600 group-hover:text-accent"></i> About Us</a></li>
                        <li><a href="portfolio.html" class="hover:text-accent transition-colors flex items-center gap-2 group"><i class="fas fa-angle-right text-xs text-gray-600 group-hover:text-accent"></i> Portfolio</a></li>
                        <li><a href="blog.html" class="hover:text-accent transition-colors flex items-center gap-2 group"><i class="fas fa-angle-right text-xs text-gray-600 group-hover:text-accent"></i> Blog</a></li>
                        <li><a href="contact.html" class="hover:text-accent transition-colors flex items-center gap-2 group"><i class="fas fa-angle-right text-xs text-gray-600 group-hover:text-accent"></i> Contact</a></li>
                    </ul>
                </div>
                
                <div>
                    <h3 class="font-display font-bold text-white text-lg mb-6 tracking-wide">Legal</h3>
                    <ul class="space-y-4 text-sm text-gray-400 font-medium">
                        <li><a href="#" class="hover:text-accent transition-colors flex items-center gap-2 group"><i class="fas fa-angle-right text-xs text-gray-600 group-hover:text-accent"></i> Privacy Policy</a></li>
                        <li><a href="#" class="hover:text-accent transition-colors flex items-center gap-2 group"><i class="fas fa-angle-right text-xs text-gray-600 group-hover:text-accent"></i> Terms of Service</a></li>
                    </ul>
                </div>
            </div>
            <div class="border-t border-white/10 pt-8 flex flex-col md:flex-row justify-between items-center gap-4 text-sm text-gray-500 font-medium">
                <p>&copy; 2026 Db WebGraph. All Rights Reserved.</p>
                <p>Designed & Built by <a href="about.html" class="text-white hover:text-accent transition-colors">Dharbindra BK</a></p>
            </div>
        </div>
    </footer>

    <button id="backToTop" aria-label="Scroll back to top" class="fixed bottom-8 right-8 w-14 h-14 rounded-full btn-primary flex items-center justify-center opacity-0 translate-y-10 pointer-events-none transition-all duration-500 z-50 shadow-2xl shadow-accent/40">
        <i class="fas fa-arrow-up"></i>
    </button>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const mobileBtn = document.getElementById('mobile-menu-btn');
            const mobileMenu = document.getElementById('mobile-menu');
            const spans = mobileBtn.querySelectorAll('span');
            
            mobileBtn.addEventListener('click', () => {
                const isOpen = !mobileMenu.classList.contains('hidden');
                if (isOpen) {
                    mobileMenu.classList.add('hidden');
                    spans[0].style.transform = 'rotate(0) translate(0)';
                    spans[1].style.opacity = '1';
                    spans[2].style.transform = 'rotate(0) translate(0)';
                } else {
                    mobileMenu.classList.remove('hidden');
                    spans[0].style.transform = 'rotate(45deg) translate(5px, 6px)';
                    spans[1].style.opacity = '0';
                    spans[2].style.transform = 'rotate(-45deg) translate(5px, -6px)';
                }
            });

            mobileMenu.querySelectorAll('a').forEach(link => {
                link.addEventListener('click', () => {
                    mobileMenu.classList.add('hidden');
                    spans[0].style.transform = 'rotate(0) translate(0)';
                    spans[1].style.opacity = '1';
                    spans[2].style.transform = 'rotate(0) translate(0)';
                });
            });

            const navbar = document.getElementById('navbar');
            const backToTop = document.getElementById('backToTop');
            
            window.addEventListener('scroll', () => {
                if (window.scrollY > 50) {
                    navbar.classList.add('glass', 'border-white/10');
                    navbar.classList.remove('border-transparent');
                } else {
                    navbar.classList.remove('glass', 'border-white/10');
                    navbar.classList.add('border-transparent');
                }

                if (window.scrollY > 500) {
                    backToTop.classList.remove('opacity-0', 'translate-y-10', 'pointer-events-none');
                } else {
                    backToTop.classList.add('opacity-0', 'translate-y-10', 'pointer-events-none');
                }
            }, { passive: true });

            backToTop.addEventListener('click', () => {
                window.scrollTo({ top: 0, behavior: 'smooth' });
            });

            const observerOptions = { root: null, rootMargin: '0px', threshold: 0.15 };
            const observer = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('active');
                        observer.unobserve(entry.target);
                    }
                });
            }, observerOptions);

            document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
        });

        function submitForm() {
            const btn = document.getElementById('submitBtn');
            const successMsg = document.getElementById('formSuccess');
            const form = document.getElementById('contactForm');
            const originalContent = btn.innerHTML;
            btn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> Sending...';
            btn.disabled = true;
            btn.classList.add('opacity-75', 'cursor-not-allowed');
            setTimeout(() => {
                btn.innerHTML = originalContent;
                btn.disabled = false;
                btn.classList.remove('opacity-75', 'cursor-not-allowed');
                if (form) form.reset();
                if (successMsg) {
                    successMsg.classList.remove('hidden');
                    setTimeout(() => successMsg.classList.add('hidden'), 5000);
                }
            }, 1500);
        }
    </script>
</body>
</html>
"""

PAGES = {
    "index.html": {
        "title": "Home",
        "content": """
        <!-- Hero Section -->
        <section class="relative min-h-[90vh] flex items-center justify-center overflow-hidden">
            <div class="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=2564&auto=format&fit=crop')] bg-cover bg-center opacity-[0.07] mix-blend-screen pointer-events-none"></div>
            <div class="absolute inset-0 bg-gradient-to-b from-transparent via-[#050505]/80 to-[#050505] pointer-events-none"></div>
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center flex flex-col items-center mt-12 md:mt-20">
                <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full glass border border-white/10 mb-8 reveal shadow-[0_0_15px_rgba(255,255,255,0.05)]">
                    <span class="flex h-2 w-2 rounded-full bg-accent animate-pulse shadow-[0_0_8px_rgba(249,115,22,1)]"></span>
                    <span class="text-xs font-semibold text-gray-200 uppercase tracking-widest">Premium Digital Agency</span>
                </div>
                <h1 class="text-5xl md:text-7xl lg:text-8xl font-display font-bold tracking-tight mb-6 reveal drop-shadow-2xl" style="transition-delay: 100ms;">
                    Design Your <br/>
                    <span class="text-gradient-accent glow-text">Digital Future</span>
                </h1>
                <p class="text-lg md:text-xl text-gray-400 max-w-2xl mx-auto mb-10 font-light leading-relaxed reveal" style="transition-delay: 200ms;">
                    We craft premium digital experiences. From high-performance websites to compelling brand identities, empowering your business to lead in the digital era.
                </p>
                <div class="flex flex-col sm:flex-row items-center justify-center gap-5 w-full reveal" style="transition-delay: 300ms;">
                    <a href="contact.html" class="w-full sm:w-auto btn-primary px-8 py-4 rounded-full font-medium text-lg flex items-center justify-center gap-3 group">
                        Start a Project <i class="fas fa-arrow-right text-sm transform group-hover:translate-x-1 transition-transform"></i>
                    </a>
                    <a href="portfolio.html" class="w-full sm:w-auto btn-secondary px-8 py-4 rounded-full font-medium text-lg flex items-center justify-center gap-2">
                        View Portfolio
                    </a>
                </div>
            </div>
            <div class="absolute bottom-0 left-0 w-full h-32 bg-gradient-to-t from-[#050505] to-transparent pointer-events-none"></div>
        </section>

        <!-- Logo Ticker -->
        <section class="py-12 border-y border-white/5 bg-[#0a0a0a]/50 backdrop-blur-md reveal">
            <div class="max-w-7xl mx-auto px-4 overflow-hidden">
                <p class="text-center text-xs text-gray-500 font-bold mb-8 uppercase tracking-[0.2em]">Trusted by innovative teams</p>
                <div class="flex justify-center flex-wrap gap-10 md:gap-20 opacity-40 grayscale hover:grayscale-0 transition-all duration-700 ease-in-out">
                    <i class="fab fa-aws text-5xl text-white hover:text-accent transition-colors duration-300 transform hover:scale-110"></i>
                    <i class="fab fa-react text-5xl text-white hover:text-[#61dafb] transition-colors duration-300 transform hover:scale-110"></i>
                    <i class="fab fa-figma text-5xl text-white hover:text-[#f24e1e] transition-colors duration-300 transform hover:scale-110"></i>
                    <i class="fab fa-node-js text-5xl text-white hover:text-[#339933] transition-colors duration-300 transform hover:scale-110"></i>
                    <i class="fab fa-google text-5xl text-white hover:text-[#4285F4] transition-colors duration-300 transform hover:scale-110"></i>
                </div>
            </div>
        </section>

        <!-- Services -->
        <section class="py-32 relative">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center max-w-3xl mx-auto mb-20 reveal">
                    <h2 class="text-accent font-semibold tracking-[0.2em] text-xs uppercase mb-4">Our Expertise</h2>
                    <h3 class="text-4xl md:text-5xl lg:text-6xl font-display font-bold text-white mb-6">Digital Excellence <br/>Delivered.</h3>
                    <p class="text-gray-400 text-lg md:text-xl">Comprehensive solutions tailored to elevate your brand's digital presence and empower your team.</p>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                    """ + "".join([
                        f"""
                        <div class="glass-card p-8 group reveal" style="transition-delay: {delay}ms;">
                            <div class="w-14 h-14 rounded-2xl bg-white/5 border border-white/10 flex items-center justify-center mb-6 group-hover:bg-{color}/10 group-hover:border-{color}/30 transition-all duration-300 group-hover:scale-110">
                                <i class="{icon} text-2xl text-gray-300 group-hover:text-{color} transition-colors"></i>
                            </div>
                            <h4 class="text-xl font-display font-bold text-white mb-3 group-hover:text-{color} transition-colors">{title}</h4>
                            <p class="text-gray-400 text-sm leading-relaxed mb-6">{desc}</p>
                            <a href="{link}" class="inline-flex items-center text-sm font-medium text-white group-hover:text-{color} transition-colors">
                                Learn more <i class="fas fa-arrow-right ml-2 transform group-hover:translate-x-1 transition-transform"></i>
                            </a>
                        </div>
                        """ for delay, icon, color, title, desc, link in [
                            ("100", "fas fa-code", "accent", "Web Development", "High-performance, scalable websites built with modern frameworks.", "web-development.html"),
                            ("200", "fas fa-pen-nib", "brand-purple", "Graphic Design", "Striking brand identities and marketing materials that captivate.", "graphic-design.html"),
                            ("300", "fas fa-chart-line", "brand-blue", "SEO & Marketing", "Data-driven strategies to improve search rankings and drive traffic.", "#"),
                            ("400", "fas fa-graduation-cap", "green-400", "Digital Training", "Practical masterclasses equipping you with independent digital skills.", "training.html")
                        ]
                    ]) + """
                </div>
            </div>
        </section>

        <!-- Portfolio Preview -->
        <section class="py-32 bg-[#080808] relative border-y border-white/5">
            <div class="absolute top-0 right-0 w-1/3 h-1/2 bg-accent/5 blur-[100px] rounded-full pointer-events-none"></div>
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
                <div class="flex flex-col md:flex-row justify-between items-end mb-16 reveal">
                    <div class="max-w-2xl">
                        <h2 class="text-accent font-semibold tracking-[0.2em] text-xs uppercase mb-4">Selected Works</h2>
                        <h3 class="text-4xl md:text-5xl lg:text-6xl font-display font-bold text-white">Featured Projects</h3>
                    </div>
                    <a href="portfolio.html" class="mt-8 md:mt-0 inline-flex items-center gap-2 text-white hover:text-accent transition-colors font-medium border-b border-white/20 pb-1 hover:border-accent">
                        View All Projects <i class="fas fa-arrow-right ml-1"></i>
                    </a>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8 lg:gap-10">
                    <div class="group relative rounded-[32px] overflow-hidden cursor-pointer reveal shadow-2xl shadow-black/50" style="transition-delay: 100ms;">
                        <div class="aspect-w-16 aspect-h-12 md:aspect-h-10 bg-[#111]">
                            <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=2426&auto=format&fit=crop" loading="lazy" class="object-cover w-full h-full transform group-hover:scale-105 transition-transform duration-700 ease-out opacity-70 group-hover:opacity-100">
                        </div>
                        <div class="absolute inset-0 bg-gradient-to-t from-[#050505] via-[#050505]/40 to-transparent flex flex-col justify-end p-8 md:p-10">
                            <div class="transform translate-y-4 group-hover:translate-y-0 transition-transform duration-500 ease-out">
                                <div class="flex flex-wrap gap-2 mb-4">
                                    <span class="px-4 py-1.5 rounded-full glass border-white/20 text-xs font-semibold text-white tracking-wide">Web App</span>
                                </div>
                                <h4 class="text-3xl font-display font-bold text-white mb-2">Fintech Dashboard Pro</h4>
                                <p class="text-gray-300 text-sm md:text-base opacity-0 group-hover:opacity-100 transition-opacity duration-500 delay-100 max-w-md">A comprehensive financial data visualization platform.</p>
                            </div>
                        </div>
                    </div>
                    <div class="group relative rounded-[32px] overflow-hidden cursor-pointer reveal shadow-2xl shadow-black/50" style="transition-delay: 200ms;">
                        <div class="aspect-w-16 aspect-h-12 md:aspect-h-10 bg-[#111]">
                            <img src="https://images.unsplash.com/photo-1600607686527-6fb886090705?q=80&w=2300&auto=format&fit=crop" loading="lazy" class="object-cover w-full h-full transform group-hover:scale-105 transition-transform duration-700 ease-out opacity-70 group-hover:opacity-100">
                        </div>
                        <div class="absolute inset-0 bg-gradient-to-t from-[#050505] via-[#050505]/40 to-transparent flex flex-col justify-end p-8 md:p-10">
                            <div class="transform translate-y-4 group-hover:translate-y-0 transition-transform duration-500 ease-out">
                                <div class="flex flex-wrap gap-2 mb-4">
                                    <span class="px-4 py-1.5 rounded-full glass border-white/20 text-xs font-semibold text-white tracking-wide">E-Commerce</span>
                                </div>
                                <h4 class="text-3xl font-display font-bold text-white mb-2">Lumina Storefront</h4>
                                <p class="text-gray-300 text-sm md:text-base opacity-0 group-hover:opacity-100 transition-opacity duration-500 delay-100 max-w-md">High-conversion headless e-commerce experience.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- About & Stats -->
        <section class="py-32 relative">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 lg:gap-24 items-center">
                    <div class="reveal">
                        <h2 class="text-accent font-semibold tracking-[0.2em] text-xs uppercase mb-4">About Us</h2>
                        <h3 class="text-4xl md:text-5xl lg:text-6xl font-display font-bold text-white mb-8 leading-tight">More Than Just <br/>An Agency.</h3>
                        <p class="text-gray-400 text-lg leading-relaxed mb-8">
                            We don't just create digital products for you; we help you learn how to create and manage them yourself.
                        </p>
                        <div class="glass-card p-6 border-l-4 border-l-accent mb-10 transform hover:translate-x-2 transition-transform duration-300">
                            <p class="text-xl font-display italic text-gray-200">"सीप सिकौँ, आत्मनिर्भर बनौँ!"</p>
                            <span class="text-sm text-gray-500 mt-2 block font-medium tracking-wide">(Learn skills, become self-reliant)</span>
                        </div>
                        <a href="about.html" class="btn-secondary px-8 py-4 rounded-full font-medium inline-flex items-center gap-3">
                            Read Our Story <i class="fas fa-arrow-right text-sm"></i>
                        </a>
                    </div>
                    <div class="grid grid-cols-2 gap-4 sm:gap-6 reveal" style="transition-delay: 200ms;">
                        <div class="glass-card p-8 lg:p-10 text-center flex flex-col items-center justify-center">
                            <span class="text-5xl font-display font-bold text-white mb-3 tracking-tighter">100+</span>
                            <span class="text-gray-400 text-xs uppercase tracking-widest font-semibold">Projects Delivered</span>
                        </div>
                        <div class="glass-card p-8 lg:p-10 text-center flex flex-col items-center justify-center lg:mt-12">
                            <span class="text-5xl font-display font-bold text-white mb-3 tracking-tighter">5+</span>
                            <span class="text-gray-400 text-xs uppercase tracking-widest font-semibold">Years Experience</span>
                        </div>
                        <div class="glass-card p-8 lg:p-10 text-center flex flex-col items-center justify-center lg:-mt-12">
                            <span class="text-5xl font-display font-bold text-white mb-3 tracking-tighter">500+</span>
                            <span class="text-gray-400 text-xs uppercase tracking-widest font-semibold">Students Trained</span>
                        </div>
                        <div class="glass-card p-8 lg:p-10 text-center flex flex-col items-center justify-center">
                            <span class="text-5xl font-display font-bold text-white mb-3 tracking-tighter">99%</span>
                            <span class="text-gray-400 text-xs uppercase tracking-widest font-semibold">Client Satisfaction</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Contact Section inline -->
        <section id="contact" class="py-32 relative overflow-hidden border-t border-white/5 bg-[#080808]">
            <div class="absolute inset-0 bg-accent/5 pointer-events-none"></div>
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
                <div class="glass-card border border-accent/20 p-8 md:p-12 lg:p-16 rounded-[40px] max-w-6xl mx-auto shadow-2xl shadow-accent/10">
                    <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
                        <div class="reveal">
                            <h2 class="text-4xl md:text-5xl lg:text-6xl font-display font-bold text-white mb-6">Let's build something <span class="text-gradient-accent glow-text">extraordinary.</span></h2>
                            <p class="text-gray-400 text-lg mb-10 leading-relaxed">Ready to elevate your digital presence or learn new skills? Drop us a message.</p>
                            <div class="space-y-8">
                                <div class="flex items-center gap-5 group">
                                    <div class="w-14 h-14 rounded-2xl glass border-white/10 flex items-center justify-center text-accent group-hover:bg-accent/10 transition-colors"><i class="fas fa-map-marker-alt text-xl"></i></div>
                                    <div>
                                        <p class="text-sm font-medium text-gray-500 uppercase tracking-widest mb-1">Location</p>
                                        <p class="text-lg text-white">Kathmandu, Nepal</p>
                                    </div>
                                </div>
                                <div class="flex items-center gap-5 group">
                                    <div class="w-14 h-14 rounded-2xl glass border-white/10 flex items-center justify-center text-accent group-hover:bg-accent/10 transition-colors"><i class="fas fa-envelope text-xl"></i></div>
                                    <div>
                                        <p class="text-sm font-medium text-gray-500 uppercase tracking-widest mb-1">Email</p>
                                        <a href="mailto:contact@dbwebgraph.com" class="text-lg text-white hover:text-accent transition-colors">contact@dbwebgraph.com</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="glass p-8 md:p-10 rounded-3xl border-white/10 reveal" style="transition-delay: 200ms;">
                            <form id="contactForm" class="space-y-5" onsubmit="event.preventDefault(); submitForm();">
                                <div><input type="text" placeholder="Your Name" class="w-full bg-[#111] border border-white/10 rounded-2xl px-5 py-4 text-white placeholder-gray-500 focus:outline-none focus:border-accent focus:ring-1 focus:ring-accent transition-all duration-300" required></div>
                                <div><input type="email" placeholder="Your Email" class="w-full bg-[#111] border border-white/10 rounded-2xl px-5 py-4 text-white placeholder-gray-500 focus:outline-none focus:border-accent focus:ring-1 focus:ring-accent transition-all duration-300" required></div>
                                <div><textarea rows="4" placeholder="Tell us about your project..." class="w-full bg-[#111] border border-white/10 rounded-2xl px-5 py-4 text-white placeholder-gray-500 focus:outline-none focus:border-accent focus:ring-1 focus:ring-accent transition-all duration-300 resize-none" required></textarea></div>
                                <button type="submit" id="submitBtn" class="w-full btn-primary py-4 rounded-2xl font-bold text-lg mt-2 flex justify-center items-center gap-2"><span>Send Message</span> <i class="fas fa-paper-plane text-sm"></i></button>
                                <p id="formSuccess" class="text-green-400 text-sm text-center hidden mt-4 font-medium"><i class="fas fa-check-circle mr-1"></i> Message sent successfully!</p>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        """
    },
    "about.html": {
        "title": "About Dharbindra BK",
        "content": """
        <section class="py-32 relative">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="flex flex-col lg:flex-row gap-16 items-center mb-24">
                    <div class="w-full lg:w-1/3 relative reveal">
                        <div class="absolute -inset-4 bg-gradient-to-br from-accent/30 to-brand-purple/30 rounded-[40px] blur-2xl z-0"></div>
                        <div class="relative rounded-[40px] overflow-hidden shadow-2xl glass border border-white/10 aspect-square flex items-center justify-center z-10 group">
                            <i class="fas fa-user-tie text-[10rem] text-gray-600 group-hover:scale-110 group-hover:text-gray-400 transition-all duration-500"></i>
                            <div class="absolute inset-0 bg-gradient-to-t from-[#050505] via-[#050505]/40 to-transparent p-6 flex flex-col justify-end text-white text-center opacity-0 group-hover:opacity-100 transition-opacity duration-500">
                                <h2 class="text-3xl font-display font-bold mb-1">Dharbindra BK</h2>
                                <p class="text-accent font-medium uppercase tracking-widest text-xs">Founder</p>
                            </div>
                        </div>
                    </div>
                    <div class="w-full lg:w-2/3 reveal" style="transition-delay: 100ms;">
                        <h1 class="text-4xl lg:text-6xl font-display font-extrabold text-white mb-3">Dharbindra BK</h1>
                        <h2 class="text-xl lg:text-2xl text-accent font-bold mb-8">Founder & Digital Skills Trainer — Db WebGraph</h2>
                        <p class="text-lg text-gray-400 mb-8 leading-relaxed">
                            Dharbindra BK is a web development and graphic design educator who focuses on teaching digital skills in a simple, practical, and student-friendly way. With a deep passion for empowering individuals, he bridges the gap between complex technology and accessible learning.
                        </p>
                        <h3 class="text-lg font-display font-bold text-white mb-5 uppercase tracking-widest text-xs">Areas of Work</h3>
                        <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                            """ + "".join([
                                f'<div class="glass-card p-5 rounded-2xl text-center group"><i class="{icon} text-3xl text-gray-500 group-hover:text-accent transition-colors mb-3 block"></i><span class="text-sm font-bold text-gray-300">{label}</span></div>'
                                for icon, label in [
                                    ("fas fa-code", "Web Dev"), ("fab fa-wordpress", "WordPress"),
                                    ("fas fa-pen-nib", "Graphic Design"), ("fas fa-bullhorn", "Digital Branding"),
                                    ("fas fa-search", "SEO"), ("fas fa-chalkboard-teacher", "Online Learning"),
                                    ("fas fa-laptop", "Computer Edu"), ("fas fa-video", "Content Creation")
                                ]
                            ]) + """
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
        <section class="py-32 relative">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center mb-20 reveal">
                    <h1 class="text-5xl lg:text-7xl font-display font-extrabold text-white mb-6">Web Development</h1>
                    <div class="w-24 h-1.5 bg-gradient-to-r from-accent to-orange-300 mx-auto rounded-full mb-8"></div>
                    <p class="text-xl text-gray-400 max-w-2xl mx-auto">Build a professional digital presence for yourself, your organization, or your business.</p>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    """ + "".join([
                        f"""
                        <div class="glass-card p-8 rounded-3xl flex flex-col group reveal" style="transition-delay: {delay}ms;">
                            <i class="{icon} text-5xl text-gray-600 mb-6 transition-colors group-hover:text-accent"></i>
                            <h3 class="text-2xl font-display font-bold text-white mb-4">{title}</h3>
                            <p class="text-gray-400 mb-6 flex-grow">{desc}</p>
                            <div class="glass p-4 rounded-xl border border-accent/20 mt-auto group-hover:bg-accent/5 transition-colors">
                                <p class="text-sm text-accent font-bold flex items-start"><i class="fas fa-graduation-cap mt-1 mr-2 text-lg"></i> Master Training Available</p>
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
    "portfolio.html": {
        "title": "Portfolio",
        "content": """
        <section class="py-32 relative">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center mb-20 reveal">
                    <h1 class="text-5xl lg:text-7xl font-display font-extrabold text-white mb-6">Our Portfolio</h1>
                    <div class="w-24 h-1.5 bg-gradient-to-r from-accent to-orange-300 mx-auto rounded-full mb-8"></div>
                    <p class="text-xl text-gray-400 max-w-2xl mx-auto">Explore some of the premium digital experiences we've crafted.</p>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8 lg:gap-10">
                    <div class="group relative rounded-[32px] overflow-hidden cursor-pointer reveal shadow-2xl shadow-black/50" style="transition-delay: 100ms;">
                        <div class="aspect-w-16 aspect-h-12 bg-[#111]">
                            <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=2426&auto=format&fit=crop" loading="lazy" class="object-cover w-full h-full transform group-hover:scale-105 transition-transform duration-700 ease-out opacity-70 group-hover:opacity-100">
                        </div>
                        <div class="absolute inset-0 bg-gradient-to-t from-[#050505] via-[#050505]/40 to-transparent flex flex-col justify-end p-8 md:p-10">
                            <div class="transform translate-y-4 group-hover:translate-y-0 transition-transform duration-500 ease-out">
                                <div class="flex flex-wrap gap-2 mb-4">
                                    <span class="px-4 py-1.5 rounded-full glass border-white/20 text-xs font-semibold text-white tracking-wide">Web App</span>
                                </div>
                                <h4 class="text-3xl font-display font-bold text-white mb-2">Fintech Dashboard Pro</h4>
                                <p class="text-gray-300 text-sm md:text-base opacity-0 group-hover:opacity-100 transition-opacity duration-500 delay-100 max-w-md">A comprehensive financial data visualization platform.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        """
    },
    "graphic-design.html": {
        "title": "Graphic Design",
        "content": """
        <section class="py-32 relative">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center reveal">
                <h1 class="text-5xl lg:text-7xl font-display font-extrabold text-white mb-6">Graphic Design</h1>
                <div class="w-24 h-1.5 bg-gradient-to-r from-accent to-orange-300 mx-auto rounded-full mb-8"></div>
                <p class="text-xl text-gray-400">Creative design that gives your brand a highly professional and memorable identity.</p>
            </div>
        </section>
        """
    },
    "training.html": {
        "title": "Training",
        "content": """
        <section class="py-32 relative">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center reveal">
                <h1 class="text-5xl lg:text-7xl font-display font-extrabold text-white mb-6">Master Training</h1>
                <div class="w-24 h-1.5 bg-gradient-to-r from-accent to-orange-300 mx-auto rounded-full mb-8"></div>
                <p class="text-xl text-gray-400">Learn the Skill. Practice the Skill. Build Your Own Work.</p>
            </div>
        </section>
        """
    },
    "education.html": { "title": "Education", "content": "<section class='py-32'><div class='max-w-7xl mx-auto px-4 text-center'><h1 class='text-5xl text-white font-display font-bold'>Education</h1></div></section>" },
    "blog.html": { "title": "Blog", "content": "<section class='py-32'><div class='max-w-7xl mx-auto px-4 text-center'><h1 class='text-5xl text-white font-display font-bold'>Blog</h1></div></section>" },
    "contact.html": { "title": "Contact", "content": "<section class='py-32'><div class='max-w-7xl mx-auto px-4 text-center'><h1 class='text-5xl text-white font-display font-bold'>Contact Us</h1></div></section>" }
}

if __name__ == "__main__":
    for filename, page_data in PAGES.items():
        filepath = os.path.join(WORKSPACE, filename)
        
        # Replace title in header
        page_header = HEADER.replace("{title}", page_data["title"])
        
        full_html = page_header + page_data["content"] + FOOTER
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(full_html)
        
        print(f"Generated {filename}")
    
    print("Site generation complete!")
