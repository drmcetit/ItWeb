import { useState, useEffect } from "react"
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap/dist/js/bootstrap.bundle.min.js"
import { Carousel } from "react-bootstrap"
import axios from "axios"

const HeroCarousel = () => {
  const slides = [
    {
      id: 1,
      image: "IT_Hero.png",
      title: "Dr. Mahalingam College of Engineering and Technology",
      dept: "Department of Information Technology",
      ctaText: "Explore Department",
      ctaLink: "#",
    },
    {
      id: 2,
      image: "Placements_Hero.png",
      title: "Empowering Future IT Professionals",
      description: "Unlock your career potential with top-tier placements. We bridge the gap between talent and opportunity.",
      ctaText: "Explore Placement",
      ctaLink: "#",
    },
    {
      id: 3,
      image: "Facilities_Hero.png",
      title: "Alpha Cloud – Your Pathway to Success",
      description: "With Alpha Cloud, stay ahead with real-time project experience, skill enhancement, and placement-driven learning",
      ctaText: "Explore Facilities",
      ctaLink: "#",
    },
    {
      id: 4,
      image: "Association_Hero.png",
      title: "InfoBee – Powering Student Innovation",
      description: "Led by students, for students! InfoBee fosters collaboration, knowledge-sharing, and industry exposure to boost your career",
      ctaText: "Explore Association",
      ctaLink: "#",
    },
  ]

  const [index, setIndex] = useState(0)
  const [isPlaying, setIsPlaying] = useState(true)

  const handleSelect = (selectedIndex) => {
    setIndex(selectedIndex)
    // Pause auto-play when user interacts
    setIsPlaying(false)
    // Resume auto-play after 5 seconds
    setTimeout(() => setIsPlaying(true), 5000)
  }

  // Auto-play functionality
  useEffect(() => {
    
    let interval

    if (isPlaying) {
      interval = setInterval(() => {
        setIndex((prevIndex) => (prevIndex === slides.length - 1 ? 0 : prevIndex + 1))
      }, 5000) // Change slide every 5 seconds
    }

    return () => {
      if (interval) clearInterval(interval)
    }
  }, [isPlaying, slides.length])

  const home =  async() => {
    try{
      const response = await axios
      .get('http://127.0.0.1:8000/api/')
      .then(response => {
        console.log(response.data)
        })
    }
    catch{
      console.log("Error", error.response.data)
    }
  }
  useEffect(()=>{
    home()
  },[])


  return (
    <>
    <div className="container mb-5" style={{marginTop:"13vh", borderRadius:"8px"}}>
        <div className="hero-carousel-container">
        <Carousel
            activeIndex={index}
            onSelect={handleSelect}
            interval={null} // We're handling the interval manually
            controls={false}
            indicators={true}
            className="hero-carousel"
            style={
                {
                    borderRadius:"8px"
                }
            }
        >
            {slides.map((slide) => (
            <Carousel.Item key={slide.id}>
                <div
                className="carousel-background"
                rel="preload"
                style={{
                    backgroundImage: `url(${slide.image})`,
                    height: "500px",
                    backgroundSize: "cover",
                    backgroundPosition: "center",
                    borderRadius: "8px",
                }}
                >
                <div className="carousel-overlay" style={{borderRadius:"8px"}}></div>
                <div className="carousel-content container d-flex align-items-center justify-content-center h-100 p-md-5" style={{borderRadius:"8px"}}>
                    <div className="text-center text-white p-md-5">
                    <h1 className="display-5 fw-bold m-0 p-0 mb-2">{slide.title}</h1>
                    <p className="fs-2 h2 mb-1 p-0 m-0 mb-1">{slide.dept}</p>
                    <p className="fs-6 fw-light p-0 m-0 mb-1">{slide.description}</p>
                    <a href={slide.ctaLink} className="btn btn-primary px-5 py-1 mt-1 m-0 fs-6">
                        {slide.ctaText}
                    </a>
                    </div>
                </div>
                </div>
            </Carousel.Item>
            ))}
        </Carousel>
        </div>
    </div>
    </>
  )
}

export default HeroCarousel

