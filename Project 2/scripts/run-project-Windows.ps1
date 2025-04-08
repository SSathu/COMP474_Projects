COMPOSE_BAKE=true docker-compose up --build -d

while ($true) {
    
    $container = docker ps --filter "name=terminal-io" --filter "status=running"
    
    if ($container -match "terminal-io") {
        Write-Host "Starting Chatbot..."
        docker attach terminal-io
        break
    } else {
        Write-Host "Waiting all images to be built and containers running..."
        Start-Sleep -Seconds 10
    }
}

cls

docker exec -it terminal-io python /terminal_io/terminal_driver.py