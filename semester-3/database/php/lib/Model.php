<?php

abstract class Model
{
    abstract public static function tableName(): string;
    /**
     * @return string[]
     */
    abstract public static function header(): array;
    abstract public function toArray(): array;
}

abstract class ModelRequestDto
{
    abstract public static function tableName(): string;

    /**
     * @return array<string, mixed>
     */
    public function nonNullEntries(): array
    {
        return array_filter($this->entries(), fn($v) => $v !== null);
    }

    /**
     * @return array<string, mixed>
     */
    public function entries(): array
    {
        $r = new ReflectionClass($this);
        $props = $r->getProperties();

        $fields = [];
        foreach ($props as $prop) {
            $fields[$prop->name] = $prop->getValue($this);
        }

        return $fields;
    }
}