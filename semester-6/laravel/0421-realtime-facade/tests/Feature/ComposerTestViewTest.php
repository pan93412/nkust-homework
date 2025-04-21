<?php


test('should contain "這是來自 ComposerServiceProvider 的全域變數" in composer-test view', function () {
    $response = $this->view('composer-test');

    $response->assertSee('這是來自 ComposerServiceProvider 的全域變數');
});
