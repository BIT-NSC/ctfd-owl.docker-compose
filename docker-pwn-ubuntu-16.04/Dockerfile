FROM ctftraining/base_pwn_xinetd

COPY src/pwn /home/ctf/pwn

RUN chown root:ctf /home/ctf/pwn && \
    chmod 750 /home/ctf/pwn && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*