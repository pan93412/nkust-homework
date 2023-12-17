<?php

class Meta
{
    public int $fieldNums;
    public int $recordNums;

    /**
     * @var FieldMeta[]
     */
    public array $fieldMeta = [];

    public function __construct(
        public string $database,
        mysqli_result $result,
    ) {
        $this->fieldNums = $result->field_count;
        $this->recordNums = intval($result->num_rows);
        while ($meta = $result->fetch_field()) {
            $this->fieldMeta[] = new FieldMeta($meta);
        }
    }
}

class FieldMeta
{
    public string $name;
    public string $table;
    public int $maxLength;
    public string $type;

    public function __construct(
        public object $meta
    ) {
        $this->name = $meta->name;
        $this->table = $meta->table;
        $this->maxLength = $meta->max_length;
        $this->type = $meta->type;
    }
}