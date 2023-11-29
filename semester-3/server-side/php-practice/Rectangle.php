<?php

class Rectangle
{
    private float $width;
    private float $height;

    public function __construct(float $width = 0.0, float $height = 0.0)
    {
        $this->width = $width;
        $this->height = $height;
    }

    public function getWidth(): float
    {
        return $this->width;
    }

    public function getHeight(): float
    {
        return $this->height;
    }

    public function getArea(): float
    {
        return $this->width * $this->height;
    }

    public function setHeight(float $height): void
    {
        $this->height = $height;
    }

    public function setWidth(float $width): void
    {
        $this->width = $width;
    }

    public function __toString(): string
    {
        return "Rectangle({$this->getWidth()} × {$this->getHeight()})";
    }
}
