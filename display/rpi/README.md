# Configure OLED display

### Normal

```bash
python3 test.py -d sh1106 -i spi --width 128 --height 64
```

### Docker

```bash
docker build -t rpi-cluster/display .
docker run --privileged -d --name oled --restart=unless-stopped rpi-cluster/display:latest
```
