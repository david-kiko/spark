#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
FROM openjdk:8-jre-slim-bullseye

ENV DEBIAN_FRONTEND="noninteractive"

COPY config/pip.conf /tmp/pip.conf

RUN sed -i -E 's#http://(deb|security).debian.org#http://mirrors.aliyun.com#g' /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -o Acquire::Retries=5 --no-install-recommends -y \
      wget \
      curl \
      gosu \
      vim \
      krb5-user \
      python3 \
      python3-pip && \
    apt-get clean && \
    mkdir $HOME/.pip/ && \
    cp -f /tmp/pip.conf $HOME/.pip/ && \
    ln -s /usr/bin/python3 /usr/bin/python

ENV SPARK_HOME="/opt/spark"
ENV PATH="${SPARK_HOME}/bin:${PATH}"

COPY bin/decom.sh /opt/
COPY bin/entrypoint.sh /opt/

RUN apt-get install -y -o Acquire::Retries=5 --no-install-recommends \
  bash tini libc6 libpam-modules libnss3 procps net-tools && \
  apt-get clean && \
  python -m pip install --no-cache-dir \
  numpy==1.21.6 pandas==1.3.5 pyarrow==10.0.1

# spark
COPY spark-*.tgz /

RUN tar xzf spark-*.tgz -C /opt && \
  rm spark-*.tgz && \
  mv /opt/spark-* /opt/spark && \
  mkdir -p \
  /opt/spark/work-dir \
  /opt/spark/logs \
  /etc/spark/conf \
  /etc/metrics/conf/ && \
  chmod g+w /opt/spark/work-dir && \
  chmod a+x /opt/decom.sh && \
  chmod 777 -R /tmp/ && \
  echo "auth required pam_wheel.so use_uid" >> /etc/pam.d/su && \
  chgrp root /etc/passwd && chmod ug+rw /etc/passwd


ARG HIVE_VERSION="3.1.3"

ENV SPARK_DIST_CLASSPATH="/opt/apache-hive-${HIVE_VERSION}-bin/lib/*"
# hive on spark 的 pod 不需要 python 文件。
# 要删除所有 hive 2.3.9 的依赖，否则会与 hive-exec 冲突。
# 将 orc/parquet 替换成与 hive 中的版本一致。(hive-exec 中包含了 parquet 的支持，这里仅更新 orc)
RUN rm -f /opt/spark/jars/hive-*.jar && \
    rm -f /opt/spark/jars/orc-*.jar && \
    rm -f /opt/spark/jars/parquet-*.jar && \
    rm -rf /opt/spark/python/ && \
    mkdir -p /opt/apache-hive-${HIVE_VERSION}-bin/lib/

COPY apache-hive-${HIVE_VERSION}-bin.tar.gz ./
RUN tar -xzf apache-hive-${HIVE_VERSION}-bin.tar.gz -C /tmp && \
    cp /tmp/apache-hive-${HIVE_VERSION}-bin/lib/hive-exec-${HIVE_VERSION}.jar /opt/apache-hive-${HIVE_VERSION}-bin/lib/ && \
    cp /tmp/apache-hive-${HIVE_VERSION}-bin/lib/hive-kryo-registrator-${HIVE_VERSION}.jar /opt/apache-hive-${HIVE_VERSION}-bin/lib/ && \
    cp /tmp/apache-hive-${HIVE_VERSION}-bin/lib/orc-core-1.5.8.jar /opt/apache-hive-${HIVE_VERSION}-bin/lib/ && \
    cp /tmp/apache-hive-${HIVE_VERSION}-bin/lib/orc-shims-1.5.8.jar /opt/apache-hive-${HIVE_VERSION}-bin/lib/ && \
    cp /tmp/apache-hive-${HIVE_VERSION}-bin/lib/orc-tools-1.5.8.jar /opt/apache-hive-${HIVE_VERSION}-bin/lib/ && \
    rm -r /tmp/apache-hive-${HIVE_VERSION}-bin && \
    rm apache-hive-${HIVE_VERSION}-bin.tar.gz

Run touch 1 && rm 1

WORKDIR /opt/spark/work-dir
RUN chmod g+w /opt/spark/work-dir
RUN chmod a+x /opt/decom.sh
RUN chmod a+x /opt/entrypoint.sh

ENTRYPOINT [ "/opt/entrypoint.sh" ]