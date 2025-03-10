<?php

namespace App\Services;

final readonly class DemoMessageService
{
    public function __construct(
        private NowDateHelper $nowDateHelper,
    ) {
    }

    public function getMessage(): array {
        return [
            'current_time' => $this->nowDateHelper->getNowTime(),
            'author' => 'Yi-Jyun Pan',
            'experise' => ['backend', 'cloud'],
            'message' => 'Hello, welcome to my demo message service!',
        ];
    }
}
