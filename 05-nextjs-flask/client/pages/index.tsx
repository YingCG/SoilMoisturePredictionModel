import React, {useEffect, useState} from 'react'

interface WeatherData {
  message: string;
  rain: number[];
  airTemp: number[];
  soilTemp: number[];
  soilMoisture: number[];
}

function index() {
  const [message, setMessage] = useState("Loading")
  const [weatherData, setWeatherData] = useState<WeatherData | null>(null);

  useEffect(() => {
    fetch("http://localhost:8080/").then(
      response => response.json()
    ).then((data) => {
      console.log(data)
      setMessage(data.message)
      console.log(data.rain)
      setWeatherData(data)
    })
  }, [])

  return (
    <div>
      {message}
      {weatherData && Object.keys(weatherData).map((key) => (
          key !== "message" && Array.isArray(weatherData[key as keyof WeatherData]) && (
            <div key={key}>
              <h2>{key.charAt(0).toUpperCase() + key.slice(1)} Data:</h2>
              {(weatherData[key as keyof WeatherData] as number[]).map((item, index) => (
                <p key={index}>{item}</p>
              ))}
            </div>
          )
        ))}
    </div>
  )
}

export default index;
