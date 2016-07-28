<?php

/*
 * Copyright 2016 trivago GmbH
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

namespace Trivago\Tas\Response\HotelCollection;

class ResultInfo
{
    /**
     * @var int
     */
    private $minPrice;

    /**
     * @var int
     */
    private $maxPrice;

    /**
     * @var string
     */
    private $currency;

    public function __construct(array $data)
    {
        $price = $data['price'];
        $this->minPrice = $price['min'];
        $this->maxPrice = $price['max'];
        $this->currency = $price['currency'];
    }

    /**
     * @return int
     */
    public function getMinPrice()
    {
        return $this->minPrice;
    }

    /**
     * @return int
     */
    public function getMaxPrice()
    {
        return $this->maxPrice;
    }

    /**
     * @return string
     */
    public function getCurrency()
    {
        return $this->currency;
    }
}
